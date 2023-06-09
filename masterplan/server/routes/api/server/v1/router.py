import os
from masterplan.server import models
import fastapi
from fastapi import Depends
from masterplan.server import crud
from masterplan.server import deps
from masterplan.database.engine import Session
from masterplan.database import tables
from masterplan.server.authentication import auth
import pkg_resources

router = fastapi.routing.APIRouter(
    prefix="/api/server/v1",
    tags=["Server v1"]
)


@router.get("/", response_model=models.full.ServerFull)
async def read_self(server=fastapi.Depends(deps.dep_server)):
    return server


@router.put("/", dependencies=[Depends(auth.implicit_scheme)], response_model=models.full.ServerFull)
async def edit_self(new_server: models.edit.ServerEdit, current_user: tables.User = fastapi.Depends(deps.dep_admin),
                    session: Session = fastapi.Depends(deps.dep_session), server=fastapi.Depends(deps.dep_server)):
    crud.quick_update(session, server, new_server)
    return server


@router.get("/planetarium", response_model=models.full.Planetarium)
async def read_self(server=fastapi.Depends(deps.dep_server)):
    return models.full.Planetarium(type="Masterplan",
                                   version="0.1",
                                   oauth_public=os.environ["OAUTH_PUBLIC"], domain=os.environ["DOMAIN"],
                                   audience=os.environ["API_AUDIENCE"], server=server)
