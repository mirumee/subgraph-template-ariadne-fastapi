from ariadne.asgi import GraphQL
from fastapi import FastAPI
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
