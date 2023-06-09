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
    description='Fill database and elastic with test data from "posts.csv"',
    tags=[
        "Tools"
    ]
)
def _fill_database():
    return ActionRepository.fill_database()


@app.get(
    "/clear_db",
    response_class=JSONResponse,
    description='Deletes all data from database and elastic',
    tags=[
        "Tools"
    ]
)
def _clear_database():
    return ActionRepository.clear_database()
