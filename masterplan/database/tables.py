import uuid
import os

import sqlalchemy.orm
import requests
from sqlalchemy import Table, Column, String, LargeBinary, ForeignKey, JSON, DateTime, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import datetime

__all__ = (
    "Base",
    "User",
    "Server",
)

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(LargeBinary, nullable=True)
    is_planner = Column(Boolean, default=False)

    admin_of = relationship("Server", back_populates="admin")
    parts = relationship("Part", back_populates="user")


class Event(Base):
    __tablename__ = "event"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    open_until = Column(DateTime, nullable=True)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime)
    hidden = Column(Boolean, default=False)

    parts = relationship("Part", back_populates="event")


class Part(Base):
    __tablename__ = "part"

    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    event_id = Column(UUID(as_uuid=True), ForeignKey("event.id"), primary_key=True)
    join_time = Column(DateTime, nullable=False, default=datetime.datetime.now)

    user = relationship("User", back_populates="parts")
    event = relationship("Event", back_populates="parts")


class Server(Base):
    __tablename__ = "server"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    motd = Column(String)
    logo_uri = Column(String)
    custom_colors = Column(JSON)

    admin_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    admin = relationship("User", back_populates="admin_of")
