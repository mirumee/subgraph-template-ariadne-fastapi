from pathlib import Path

from ariadne import ObjectType, load_schema_from_path
from ariadne.contrib.federation import FederatedObjectType, make_federated_schema


HERE = Path(__file__).parent


query = ObjectType("Query")


@query.field("foo")
def resolve_foo(*_, id: str):
    return {"id": id, "name": "Foo"}


foo = FederatedObjectType("Foo")


@foo.reference_resolver
def resolve_foo_reference(_, _info, representation):
    return {"id": representation["id"], "name": "Foo"}


type_defs = load_schema_from_path(str(HERE / "schema.graphql"))

schema = make_federated_schema(type_defs, query, foo)
