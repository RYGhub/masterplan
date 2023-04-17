import json
from masterplan.database import tables, engine
from masterplan.server import crud
from masterplan.server.deps.database import dep_session
from masterplan.server.errors import ResourceNotFound
import fastapi
from masterplan.server.models.edit import Colors

__all__ = (
    "dep_server",
)


def dep_server(session: engine.Session = fastapi.Depends(dep_session)):
    try:
        server = crud.quick_retrieve(session, tables.Server)
    except ResourceNotFound:
        server = crud.quick_create(session, tables.Server(name="Unconfigured Masterplan Server",
                                                          motd="As an administrator, please configure me.",
                                                          logo_uri="",
                                                          custom_colors={"foreground": "none", "background": "none",
                                                                         "accent": "none"}))
    return server
