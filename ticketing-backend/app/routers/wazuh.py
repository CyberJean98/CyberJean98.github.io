import json
import os

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/webhooks/wazuh", tags=["wazuh"])

# Shared secret so random internet traffic can't create tickets in your name.
# Set this as an env var and configure the same value in Wazuh's integration.
WEBHOOK_SECRET = os.getenv("WAZUH_WEBHOOK_SECRET", "dev-only-webhook-secret")

# Alerts below this Wazuh rule level are ignored (Wazuh levels run 0-15+;
# 7+ is a reasonable "worth a ticket" cutoff to start with, tune as needed).
MIN_RULE_LEVEL = int(os.getenv("WAZUH_MIN_RULE_LEVEL", "7"))


def _severity_from_level(level: int) -> models.Severity:
    if level >= 12:
        return models.Severity.critical
    if level >= 10:
        return models.Severity.high
    if level >= 7:
        return models.Severity.medium
    return models.Severity.low


@router.post("/alert", status_code=201)
def receive_alert(
    alert: schemas.WazuhAlert,
    x_webhook_secret: str = Header(default=""),
    db: Session = Depends(get_db),
):
    if x_webhook_secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=401, detail="Invalid webhook secret")

    if alert.rule_level < MIN_RULE_LEVEL:
        return {"skipped": True, "reason": f"level {alert.rule_level} below threshold"}

    title = f"[Wazuh] {alert.rule_description}"
    if alert.agent_name:
        title += f" ({alert.agent_name})"

    ticket = models.Ticket(
        title=title[:255],
        description=alert.full_log or alert.rule_description,
        severity=_severity_from_level(alert.rule_level),
        status=models.Status.open,
        source=models.Source.wazuh,
        is_demo=False,  # real lab data — admin-only, never shown to visitors
        raw_alert=json.dumps(alert.model_dump()),
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    log = models.AuditLogEntry(
        ticket_id=ticket.id, actor="wazuh", action="created",
        detail=f"auto-created from rule_id={alert.rule_id}, level={alert.rule_level}",
    )
    db.add(log)
    db.commit()

    return {"ticket_id": ticket.id, "severity": ticket.severity}
