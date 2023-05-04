import typing as t
from uuid import UUID

from pydantic import typing

from masterplan.server.models import base
from datetime import datetime

__all__ = (
    "UserEdit",
    "ServerEdit",
    "EventEdit"
)


class UserEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.User`.
    """

    username: str

    class Config(base.ApiORMModel.Config):
        schema_extra = {
            "example": {
                "username": "Nemesis",
            },
        }


class Colors(base.ApiModel):
    foreground: str
    background: str
    accent: str


class ServerEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.Server`.
    """

    name: str
    motd: str
    logo_uri: t.Optional[str]
    custom_colors: t.Optional[Colors]


class EventEdit(base.ApiORMModel):
    """
    **Edit** model for :class:`.database.tables.Event`.
    """

    title: str
    description: str
    open_until: datetime
    start: datetime
    end: datetime
    hidden: bool