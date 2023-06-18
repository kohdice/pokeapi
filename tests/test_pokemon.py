from fastapi.testclient import TestClient

from pokeapi import main


class TestPokemon:
    def test_read_pokemon(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon")

        assert responce.status_code == 200
        assert responce.json() == {"Name": "けつばん"}

    def test_read_pokemon_by_name(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/name/けつばん")

        assert responce.status_code == 200
        assert responce.json() == {"Name": "けつばん"}

    def test_read_pokemon_by_name_none(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/name/")

        assert responce.status_code == 404
        assert responce.json() == {"detail": "Not Found"}

    def test_read_pokemon_by_pokedex_number(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/pokedex_number/152")

        assert responce.status_code == 200
        assert responce.json() == {
            "national_pokedex_number": 152,
            "name": "けつばん",
        }

    def test_read_pokemon_by_pokedex_number_none(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/pokedex_number/")

        assert responce.status_code == 404
        assert responce.json() == {"detail": "Not Found"}
