from fastapi.testclient import TestClient

from pokeapi import main


class TestMain:
    def test_read_root(self) -> None:
        client = TestClient(main.app)
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to Pokédex!"}
