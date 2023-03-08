from http import HTTPStatus
from os import environ
from typing import Awaitable, Callable

from ariadne.asgi import GraphQL
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from api.schema import schema


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://studio.apollographql.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/", GraphQL(schema))


@app.middleware("http")
async def check_router_security(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    router_secret = environ.get("ROUTER_SECRET")
    if router_secret is None:
        return await call_next(request)
    if request.headers.get("Router-Authorization") != router_secret:
        return Response(status_code=HTTPStatus.UNAUTHORIZED)
    return await call_next(request)
