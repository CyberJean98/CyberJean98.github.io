import enum
from datetime import datetime

from sqlalchemy import (
    Column, Integer, String, Text, DateTime, Enum, ForeignKey, Boolean
)
from sqlalchemy.orm import relationship

from .database import Base


class Severity(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class Status(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"


class Source(str, enum.Enum):
    manual = "manual"
    wazuh = "wazuh"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="visitor")  # visitor, admin
    created_at = Column(DateTime, default=datetime.utcnow)

    tickets_assigned = relationship("Ticket", back_populates="assignee")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, default="")
    severity = Column(Enum(Severity), default=Severity.low, nullable=False)
    status = Column(Enum(Status), default=Status.open, nullable=False)
    source = Column(Enum(Source), default=Source.manual, nullable=False)

    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    assignee = relationship("User", back_populates="tickets_assigned")

    # True = visible in the public sandbox, created by/for non-admin visitors.
    # False = real ticket (admin-created, or a real Wazuh alert) — admin-only.
    is_demo = Column(Boolean, default=True, nullable=False)

    raw_alert = Column(Text, nullable=True)  # original Wazuh alert JSON, if applicable

    # A category tag ("security" / "helpdesk") to help visitors filter and
    # to signal what kind of skill each ticket exercises.
    category = Column(String, nullable=True)

    # Optional troubleshooting hint, written by the admin, revealed on request
    # in the UI. Lets this double as a practice/training tool, not just a demo.
    hint = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)

    notes = relationship("TicketNote", back_populates="ticket", cascade="all, delete-orphan")
    audit_log = relationship("AuditLogEntry", back_populates="ticket", cascade="all, delete-orphan")


class TicketNote(Base):
    __tablename__ = "ticket_notes"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    author = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    ticket = relationship("Ticket", back_populates="notes")


class AuditLogEntry(Base):
    __tablename__ = "audit_log"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    actor = Column(String, nullable=False)
    action = Column(String, nullable=False)  # e.g. "status_change", "assigned"
    detail = Column(String, nullable=True)   # e.g. "open -> in_progress"
    created_at = Column(DateTime, default=datetime.utcnow)

    ticket = relationship("Ticket", back_populates="audit_log")
