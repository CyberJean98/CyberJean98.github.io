from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from .models import Severity, Status, Source


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True


class TicketNoteCreate(BaseModel):
    body: str


class TicketNoteOut(BaseModel):
    id: int
    author: str
    body: str
    created_at: datetime

    class Config:
        from_attributes = True


class TicketCreate(BaseModel):
    title: str
    description: str = ""
    severity: Severity = Severity.low
    category: Optional[str] = None  # e.g. "security", "helpdesk" — freeform


class TicketUpdate(BaseModel):
    status: Optional[Status] = None
    severity: Optional[Severity] = None
    assignee_id: Optional[int] = None
    hint: Optional[str] = None  # admin-only: see enforcement in the router


class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    severity: Severity
    status: Status
    source: Source
    category: Optional[str]
    hint: Optional[str]
    assignee_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    resolved_at: Optional[datetime]
    notes: List[TicketNoteOut] = []

    class Config:
        from_attributes = True


class WazuhAlert(BaseModel):
    """Minimal shape we expect from a Wazuh webhook / active-response payload.
    Adjust field names to match your actual Wazuh output config."""
    rule_id: Optional[str] = None
    rule_description: str
    rule_level: int
    agent_name: Optional[str] = None
    full_log: Optional[str] = None
