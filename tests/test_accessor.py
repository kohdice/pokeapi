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
        actual = accessor.search_pokemon(query)

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
        actual = accessor.search_pokemon(query)

        assert actual == []
