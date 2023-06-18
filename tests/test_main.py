from fastapi.testclient import TestClient

from pokeapi import main


class TestMain:
    def test_read_root(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/")

        assert responce.status_code == 200
        assert responce.json() == {"Prof. Oak": "Welcome to Pokédex!"}
