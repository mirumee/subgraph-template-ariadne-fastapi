from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_read_main():
    response = client.post("/graphql", json={"query": "{ foo(id: 1) { id name } }"})
    assert response.status_code == 200
    assert response.json() == {"data": {"foo": {"id": "1", "name": "Foo"}}}
