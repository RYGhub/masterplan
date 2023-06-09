import typing
from uuid import UUID
from masterplan.server.models import edit
from masterplan.server.models import base

__all__ = (
    "UserRead",
    "ServerRead",
    "EventRead"
)


class UserRead(base.ApiORMModel):
    """
    **Read** model for :class:`.database.tables.User`.
    """

    id: UUID
    username: str
    email: str

    class Config(edit.UserEdit.Config):
        schema_extra = {
            "example": {
                **edit.UserEdit.Config.schema_extra["example"],
                "id": "70fd1bf3-69dd-4cde-9d41-42368221849f",
            },
        }


class ServerRead(edit.ServerEdit):
    """
    **Read** model for :class:`.database.tables.Server`.
    """

    id: UUID


class EventRead(edit.EventEdit):
    """
    **Read** model for :class:`.database.tables.Event`.
    """

    id: UUID