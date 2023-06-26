from typing import Any

from fastapi.testclient import TestClient

from pokeapi import main


class TestPokemonRouter:
    def test_read_pokemon(self) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon")

        assert response.status_code == 200
        for pokemon in response.json():
            assert pokemon["name"] in [
                "フシギダネ",
                "フシギソウ",
                "フシギバナ",
                "メガフシギバナ",
                "ヒトカゲ",
                "リザード",
                "リザードン",
                "メガリザードンＸ",
                "メガリザードンＹ",
                "ゼニガメ",
                "カメール",
                "カメックス",
                "メガカメックス",
                "ピカチュウ",
                "ライチュウ",
                "オタチ",
                "オオタチ",
                "ミュウツー",
                "メガミュウツーＸ",
                "メガミュウツーＹ",
                "ミュウ",
                "カイオーガ",
                "ゲンシカイオーガ",
                "グラードン",
                "ゲンシグラードン",
                "ミミッキュ",
            ]

    def test_read_pokemon_by_name(self) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/name/フシギダネ")

        assert response.status_code == 200
        assert response.json() == [
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

    def test_read_pokemon_by_name_none(self) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/name/")

        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}

    def test_read_pokemon_by_pokedex_number(self) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/pokedex_number/1")

        assert response.status_code == 200
        assert response.json() == [
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
        response = client.get("/pokemon/pokedex_number/0")

        assert response.status_code == 200
        assert response.json() == []

    def test_read_pokemon_by_pokedex_number_str(self) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/pokedex_number/hoge")

        assert response.status_code == 422
        assert response.json() == {
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
        response = client.get("/pokemon/pokedex_number/")

        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}

    def test_read_pokemon_by_conditions_str(
        self, setup_conditions_mimikkyu_res: list[dict[str, Any]]
    ) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/conditions?ability_1=ばけのかわ")

        assert response.status_code == 200
        assert response.json() == setup_conditions_mimikkyu_res

    def test_read_pokemon_by_conditions_bool(
        self, setup_conditions_bool_res: list[dict[str, Any]]
    ) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/conditions?has_male=0")

        assert response.status_code == 200
        assert response.json() == setup_conditions_bool_res

    def test_read_pokemon_by_conditions_multi_param(
        self, setup_conditions_mimikkyu_res: list[dict[str, Any]]
    ) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/conditions?ability_1=ばけのかわ&has_male=1")

        assert response.status_code == 200
        assert response.json() == setup_conditions_mimikkyu_res

    def test_read_pokemon_by_conditions_none(
        self, setup_null_conditions_res: list[dict[str, Any]]
    ) -> None:
        client = TestClient(main.app)
        response = client.get("/pokemon/conditions/")

        assert response.status_code == 200
        assert response.json() == setup_null_conditions_res
