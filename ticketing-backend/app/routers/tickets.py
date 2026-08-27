from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(prefix="/tickets", tags=["tickets"])


def _log(db: Session, ticket_id: int, actor: str, action: str, detail: str = None):
    entry = models.AuditLogEntry(ticket_id=ticket_id, actor=actor, action=action, detail=detail)
    db.add(entry)


def _scope_to_user(query, current_user: models.User):
    """Visitors only ever see the public sandbox (is_demo=True).
    Admin (you) sees everything, including real Wazuh-sourced tickets."""
    if current_user.role != "admin":
        query = query.filter(models.Ticket.is_demo.is_(True))
    return query


def _get_scoped_ticket(db: Session, ticket_id: int, current_user: models.User) -> models.Ticket:
    query = _scope_to_user(db.query(models.Ticket).filter(models.Ticket.id == ticket_id), current_user)
    ticket = query.first()
    if not ticket:
        # Same 404 whether the ticket doesn't exist or the visitor just can't
        # see it — don't leak that real, non-demo tickets exist.
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.get("/", response_model=List[schemas.TicketOut])
def list_tickets(
    status: Optional[models.Status] = None,
    severity: Optional[models.Severity] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    query = _scope_to_user(db.query(models.Ticket), current_user)
    if status:
        query = query.filter(models.Ticket.status == status)
    if severity:
        query = query.filter(models.Ticket.severity == severity)
    if category:
        query = query.filter(models.Ticket.category == category)
    return query.order_by(models.Ticket.created_at.desc()).all()


@router.get("/{ticket_id}", response_model=schemas.TicketOut)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return _get_scoped_ticket(db, ticket_id, current_user)


@router.post("/", response_model=schemas.TicketOut, status_code=201)
def create_ticket(
    payload: schemas.TicketCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    # Visitors can only ever create sandbox tickets. Only admin can create a
    # "real" (non-demo) manual ticket.
    is_demo = current_user.role != "admin"

    ticket = models.Ticket(
        title=payload.title,
        description=payload.description,
        severity=payload.severity,
        source=models.Source.manual,
        is_demo=is_demo,
        category=payload.category or ("visitor-submitted" if is_demo else None),
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    _log(db, ticket.id, current_user.username, "created")
    db.commit()
    return ticket


@router.patch("/{ticket_id}", response_model=schemas.TicketOut)
def update_ticket(
    ticket_id: int,
    payload: schemas.TicketUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    ticket = _get_scoped_ticket(db, ticket_id, current_user)

    if payload.status is not None and payload.status != ticket.status:
        _log(db, ticket.id, current_user.username, "status_change",
             f"{ticket.status} -> {payload.status}")
        ticket.status = payload.status
        if payload.status == models.Status.resolved:
            ticket.resolved_at = datetime.utcnow()

    if payload.severity is not None and payload.severity != ticket.severity:
        _log(db, ticket.id, current_user.username, "severity_change",
             f"{ticket.severity} -> {payload.severity}")
        ticket.severity = payload.severity

    if payload.assignee_id is not None and payload.assignee_id != ticket.assignee_id:
        _log(db, ticket.id, current_user.username, "assigned",
             f"assignee_id -> {payload.assignee_id}")
        ticket.assignee_id = payload.assignee_id

    if payload.hint is not None:
        if current_user.role != "admin":
            raise HTTPException(status_code=403, detail="Only admin can add or edit hints")
        _log(db, ticket.id, current_user.username, "hint_updated")
        ticket.hint = payload.hint

    db.commit()
    db.refresh(ticket)
    return ticket


@router.post("/{ticket_id}/notes", response_model=schemas.TicketNoteOut, status_code=201)
def add_note(
    ticket_id: int,
    payload: schemas.TicketNoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    ticket = _get_scoped_ticket(db, ticket_id, current_user)

    note = models.TicketNote(ticket_id=ticket.id, author=current_user.username, body=payload.body)
    db.add(note)
    _log(db, ticket.id, current_user.username, "note_added")
    db.commit()
    db.refresh(note)
    return note
