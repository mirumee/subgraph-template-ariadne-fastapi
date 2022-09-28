from pathlib import Path

from ariadne import ObjectType, load_schema_from_path
from ariadne.contrib.federation import FederatedObjectType, make_federated_schema


HERE = Path(__file__).parent


query = ObjectType("Query")


@query.field("thing")
def resolve_thing(*_, id: str):
    return {"id": id, "name": "Thing"}


thing = FederatedObjectType("Thing")


@thing.reference_resolver
def resolve_thing_reference(_, _info, representation):
    return {"id": representation["id"], "name": "Thing"}


type_defs = load_schema_from_path(str(HERE / "schema.graphql"))

schema = make_federated_schema(type_defs, query, thing)
