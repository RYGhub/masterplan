from sqlalchemy import select
import uuid
from masterplan.database import tables, engine
from masterplan.server.deps.database import dep_session
import fastapi
from masterplan.server.crud import quick_retrieve

__all__ = (
    "dep_event_all",
    "dep_event"
)


def dep_event_all(session: engine.Session = fastapi.Depends(dep_session)):
    return session.query(tables.Event).all()


def dep_event(session: engine.Session = fastapi.Depends(dep_session), event_id: str = fastapi.Query(...)):
    return quick_retrieve(session, tables.Event, id=event_id)
