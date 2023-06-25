from fastapi.testclient import TestClient

from pokeapi import main


class TestPokemon:
    def test_read_pokemon(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon")

        assert responce.status_code == 200
        assert responce.json() == {"name": "けつばん"}

    def test_read_pokemon_by_name(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/name/けつばん")

        assert responce.status_code == 200
        assert responce.json() == {"name": "けつばん"}

    def test_read_pokemon_by_name_none(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/name/")

        assert responce.status_code == 404
        assert responce.json() == {"detail": "Not Found"}

    def test_read_pokemon_by_pokedex_number(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/pokedex_number/1")

        assert responce.status_code == 200
        assert responce.json() == [
            {
                "national_pokedex_number": 1,
                "name": "フシギダネ",
                "form": None,
                "regional_variant": None,
                "is_mega_evolution": False,
                "is_primal_reversion": False,
                "is_legendary": False,
                "is_mythical": False,
                "height": 0.7,
                "weight": 6.9,
                "gender_type": {"has_female": True, "has_male": True},
                "pokemon_type": {"type_1": "くさ", "type_2": "どく"},
                "abilities": {
                    "ability_1": "しんりょく",
                    "ability_2": None,
                    "hidden_ability": "ようりょくそ",
                },
                "base_stats": {
                    "attack": 49,
                    "base_total": 318,
                    "defense": 49,
                    "hp": 45,
                    "special_attack": 65,
                    "special_defense": 65,
                    "speed": 45,
                },
            }
        ]

    def test_read_pokemon_by_pokedex_number_doesnt_exist(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/pokedex_number/0")

        assert responce.status_code == 200
        assert responce.json() == []

    def test_read_pokemon_by_pokedex_number_str(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/pokedex_number/hoge")

        assert responce.status_code == 422
        assert responce.json() == {
            "detail": [
                {
                    "loc": ["path", "pokedex_number"],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer",
                }
            ]
        }

    def test_read_pokemon_by_pokedex_number_none(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/pokedex_number/")

        assert responce.status_code == 404
        assert responce.json() == {"detail": "Not Found"}

    def test_read_pokemon_by_conditions_str(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/conditions?condition=hoge")

        assert responce.status_code == 200
        assert responce.json() == {
            "national_pokedex_number": 152,
            "name": "けつばん",
            "condition": "hoge",
        }

    def test_read_pokemon_by_conditions_int(self) -> None:
        client = TestClient(main.app)
        responce = client.get("/pokemon/conditions?condition=1")

        assert responce.status_code == 200
        assert responce.json() == {
            "national_pokedex_number": 152,
            "name": "けつばん",
            "condition": 1,
        }
