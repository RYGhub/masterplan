import os
import uuid

from masterplan.server.models import edit, read, full
import fastapi
from fastapi import Depends
from masterplan.server import crud
from masterplan.server import deps
from masterplan.database.engine import Session
from masterplan.database import tables
from masterplan.server.authentication import auth
from pydantic.typing import List

router = fastapi.routing.APIRouter(
    prefix="/api/event/v1",
    tags=["Event v1"]
)


@router.get("/", response_model=List[read.EventRead])
async def read_all(events=fastapi.Depends(deps.dep_event_all)):
    return events


@router.get("/{event_id}", response_model=full.EventFull)
async def read_event(event_id: str, event=fastapi.Depends(deps.dep_event)):
    return event


@router.post("/", dependencies=[Depends(auth.implicit_scheme)], response_model=full.EventFull)
async def create_event(data: edit.EventEdit, session=fastapi.Depends(deps.dep_session),
                       current_user=fastapi.Depends(deps.dep_planner)):
    return crud.quick_create(session, tables.Event(title=data.title, description=data.description,
                                                   open_until=data.open_until, start=data.start,
                                                   end=data.end, hidden=data.hidden))
