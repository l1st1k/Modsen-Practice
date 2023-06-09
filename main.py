from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from repository import ActionRepository

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.get(
    "/fill_db",
    response_class=JSONResponse,
    description='Fill database with test data',
    tags=[
        "Tools"
    ]
)
def _fill_db():
    return ActionRepository.fill_database()
