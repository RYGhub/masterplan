import os
import pathlib
import fastapi
import sqlalchemy.exc
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from masterplan.server.errors import ApiException
from masterplan.server.handlers import handle_api_error, handle_sqlalchemy_not_found, \
    handle_sqlalchemy_multiple_results, handle_generic_error
from masterplan.server.routes.api.users.v1.router import router as router_api_user_v1
from masterplan.server.routes.api.server.v1.router import router as router_api_server_v1
from masterplan.server.routes.api.event.v1.router import router as router_api_event_v1
from fastapi_pagination import add_pagination

with open(pathlib.Path(__file__).parent.joinpath("description.md")) as file:
    description = file.read()

app = fastapi.FastAPI(
    debug=__debug__,
    title="Masterplan",
    description=description,
    version="0.1",
)

app.mount("/files", StaticFiles(directory="Files"), name="files")


@app.get("/")
async def root():
    return RedirectResponse(os.environ["FRONTEND_URL"], status_code=303)


app.include_router(router_api_user_v1)
app.include_router(router_api_server_v1)
app.include_router(router_api_event_v1)

app.add_exception_handler(ApiException, handle_api_error)
app.add_exception_handler(sqlalchemy.exc.NoResultFound, handle_sqlalchemy_not_found)
app.add_exception_handler(sqlalchemy.exc.MultipleResultsFound, handle_sqlalchemy_multiple_results)
app.add_exception_handler(Exception, handle_generic_error)

add_pagination(app)
