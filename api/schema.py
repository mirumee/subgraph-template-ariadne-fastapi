from pathlib import Path

from ariadne import load_schema_from_path, ObjectType
from ariadne.contrib.federation import make_federated_schema


HERE = Path(__file__).parent


query = ObjectType("Query")


@query.field("foo")
def resolve_foo(*_, id: str):
    return {"id": id, "name": "Foo"}


type_defs = load_schema_from_path(str(HERE / "schema.graphql"))

schema = make_federated_schema(type_defs, query)
