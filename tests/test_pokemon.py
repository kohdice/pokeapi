from fastapi.testclient import TestClient

from pokeapi import main


class TestPokemon:
    def test_read_pokemon(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon")

        assert responce.status_code == 200
        assert responce.json() == {"Name": "けつばん"}
