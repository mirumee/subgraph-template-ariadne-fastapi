from ariadne.asgi import GraphQL
from fastapi import FastAPI

from api.schema import schema


app = FastAPI()
app.add_route("/", GraphQL(schema))
