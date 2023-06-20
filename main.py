from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from database import list_of_posts
from repository import ActionRepository

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.on_event("startup")
async def on_startup():
    await ActionRepository.startup()


@app.get(
    "/fill_db",
    response_class=JSONResponse,
    description='Fill database and elastic with test data from "posts.csv"',
    tags=[
        "Tools"
    ]
)
async def _fill_database() -> JSONResponse:
    return await ActionRepository.fill_database()


@app.get(
    "/clear_db",
    response_class=JSONResponse,
    description='Deletes all data from database and elastic',
    tags=[
        "Tools"
    ]
)
async def _clear_database() -> JSONResponse:
    return await ActionRepository.clear_database()


@app.get(
    "/get_items_amount",
    response_class=JSONResponse,
    description='Returns amount of items in elastic index & database table',
    tags=[
        "Tools"
    ]
)
async def _get_items_amount() -> JSONResponse:
    return await ActionRepository.get_amount()


@app.get(
    "/search/{query}",
    response_model=list_of_posts,
    description='Returns 20 last posts, that includes query text',
    tags=[
        "Posts"
    ]
)
async def _search_posts(query: str) -> list_of_posts:
    return await ActionRepository.search_posts(query=query)


@app.delete(
    "/post/{post_id}",
    response_class=JSONResponse,
    description='Deletes post from database and index by its ID',
    tags=[
        "Posts"
    ]
)
async def delete_post(post_id: str) -> JSONResponse:
    return await ActionRepository.delete_by_id(post_id=post_id)
