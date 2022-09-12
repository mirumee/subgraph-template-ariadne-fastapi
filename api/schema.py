from typing import Optional
import strawberry

from strawberry.schema_directive import Location


@strawberry.schema_directive(locations=[Location.SCHEMA])
class Contact:
    name: str = strawberry.field(description="Contact title of the subgraph owner")
    url: Optional[str] = strawberry.field(
        description="URL where the subgraph's owner can be reached"
    )
    description: Optional[str] = strawberry.field(
        description="Other relevant notes can be included here; supports markdown links"
    )


@strawberry.federation.type(keys=["id"])
class Foo:
    id: strawberry.ID
    name: Optional[str]

    @classmethod
    def resolve_reference(cls, representation: dict) -> "Foo":
        return cls(id=strawberry.ID("1"), name="Foo")


@strawberry.type
class Query:
    @strawberry.field
    def foo(self, id: strawberry.ID) -> Optional[Foo]:
        return Foo(id=id, name="Foo")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str) -> str:
        return name


schema = strawberry.federation.Schema(
    Query,
    Mutation,
    schema_directives=[
        Contact(
            name="FooBar Server Team",
            url="https://myteam.slack.com/archives/teams-chat-room-url",
            description="send urgent issues to [#oncall](https://yourteam.slack.com/archives/oncall).",
        )
    ],
)
