from typing import Generator

import pytest

from pokeapi.search import accessor


# change ES_CONNECTION_URL in setup when running with devcontainer
class TestAccessor:
    @pytest.mark.usefixtures("_setup_get_config")
    def test_search_pokemon(self) -> None:
        query = {
            "query": {
                "bool": {"must": [{"term": {"national_pokedex_number": 1}}]}
            }
        }
        response = accessor.search_pokemon(query)
        actual = []
        for i in response:
            actual.append(i)

        assert actual == [
            {
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
                "form": None,
                "gender_type": {"has_female": True, "has_male": True},
                "height": 0.7,
                "is_legendary": False,
                "is_mega_evolution": False,
                "is_mythical": False,
                "is_primal_reversion": False,
                "name": "フシギダネ",
                "national_pokedex_number": 1,
                "pokemon_type": {"type_1": "くさ", "type_2": "どく"},
                "regional_variant": None,
                "weight": 6.9,
            },
        ]

    @pytest.mark.usefixtures("_setup_get_config")
    def test_search_pokemon_not_applicable(self) -> None:
        query = {
            "query": {
                "bool": {"must": [{"term": {"national_pokedex_number": 0}}]}
            }
        }
        response = accessor.search_pokemon(query)
        actual = []
        for i in response:
            actual.append(i)

        assert actual == []

    def test_create_pokemon_response(self) -> None:
        def es_response_generator() -> Generator[dict, None, None]:
            pokemon_doc_list = [
                {
                    "_source": {
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
                        "form": None,
                        "gender_type": {"has_female": True, "has_male": True},
                        "height": 0.7,
                        "is_legendary": False,
                        "is_mega_evolution": False,
                        "is_mythical": False,
                        "is_primal_reversion": False,
                        "name": "フシギダネ",
                        "national_pokedex_number": 1,
                        "pokemon_type": {"type_1": "くさ", "type_2": "どく"},
                        "regional_variant": None,
                        "weight": 6.9,
                    },
                },
                {
                    "_source": {
                        "abilities": {
                            "ability_1": "もうか",
                            "ability_2": None,
                            "hidden_ability": "サンパワー",
                        },
                        "base_stats": {
                            "attack": 52,
                            "base_total": 309,
                            "defense": 43,
                            "hp": 39,
                            "special_attack": 60,
                            "special_defense": 50,
                            "speed": 65,
                        },
                        "form": None,
                        "gender_type": {"has_female": True, "has_male": True},
                        "height": 0.6,
                        "is_legendary": False,
                        "is_mega_evolution": False,
                        "is_mythical": False,
                        "is_primal_reversion": False,
                        "name": "ヒトカゲ",
                        "national_pokedex_number": 4,
                        "pokemon_type": {"type_1": "ほのお", "type_2": None},
                        "regional_variant": None,
                        "weight": 8.5,
                    },
                },
            ]

            for doc in pokemon_doc_list:
                yield doc["_source"]

        response = accessor.create_pokemon_response(es_response_generator())

        assert response == [
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
            },
            {
                "national_pokedex_number": 4,
                "name": "ヒトカゲ",
                "form": None,
                "regional_variant": None,
                "is_mega_evolution": False,
                "is_primal_reversion": False,
                "is_legendary": False,
                "is_mythical": False,
                "height": 0.6,
                "weight": 8.5,
                "gender_type": {"has_male": True, "has_female": True},
                "pokemon_type": {"type_1": "ほのお", "type_2": None},
                "abilities": {
                    "ability_1": "もうか",
                    "ability_2": None,
                    "hidden_ability": "サンパワー",
                },
                "base_stats": {
                    "hp": 39,
                    "attack": 52,
                    "defense": 43,
                    "special_attack": 60,
                    "special_defense": 50,
                    "speed": 65,
                    "base_total": 309,
                },
            },
        ]

    def test_create_pokemon_response_enpty(self) -> None:
        def es_response_generator_empty() -> Generator:
            empty_list: list = []
            for doc in empty_list:
                yield doc["_source"]

        response = accessor.create_pokemon_response(
            es_response_generator_empty()
        )

        assert response == []
