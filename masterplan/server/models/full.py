import typing
from masterplan.server.models import read, base

__all__ = ("UserFull",
           "ServerFull",
           "Planetarium",)


class ServerFull(read.ServerRead):
    """
    **Full** model for :class:`.database.tables.Dictionary`.
    """

    admin: typing.Optional[read.UserRead]


class Planetarium(base.ApiModel):
    """
    **Planetarium-compliant** model for :class:`.database.tables.Server`.
    """

    version: str
    type: str
    oauth_public: str
    audience: str
    domain: str

    server: ServerFull

class UserFull(read.UserRead):
    pass