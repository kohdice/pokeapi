from typing import Any

import pytest

from pokeapi.search import param


@pytest.mark.param()
class TestAbstractParam:
    class SubParam(param.Param):
        def create_param(self) -> dict[str, Any] | None:
            return None

    class ErrorSubParam(param.Param):
        pass

    def test_create_param(self) -> None:
        p = self.SubParam()
        actual = p.create_param()

        assert actual is None

    def test_not_implemented(self) -> None:
        with pytest.raises(TypeError):
            self.ErrorSubParam()  # type: ignore


@pytest.mark.param()
class TestCreatePokedexNumberParam:
    def test_create_pokedex_number_param(self) -> None:
        p = param.CreatePokedexNumberParam(1)
        actual = p.create_param()

        assert actual == {"term": {"national_pokedex_number": 1}}

    def test_create_pokedex_number_param_none(self) -> None:
        p = param.CreatePokedexNumberParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateNameParam:
    def test_create_name_param(self) -> None:
        p = param.CreateNameParam("フシギダネ")
        actual = p.create_param()

        assert actual == {"term": {"name": "フシギダネ"}}

    def test_create_name_param_none(self) -> None:
        p = param.CreateNameParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateformParam:
    def test_create_form_param(self) -> None:
        p = param.CreateFormParam("れいじゅうフォルム")
        actual = p.create_param()

        assert actual == {"term": {"form.keyword": "れいじゅうフォルム"}}

    def test_create_form_param_none(self) -> None:
        p = param.CreateFormParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateRegionalVariantParam:
    def test_create_regional_variant_param(self) -> None:
        p = param.CreateRegionalVariantParam("アローラのすがた")
        actual = p.create_param()

        assert actual == {"term": {"regional_variant.keyword": "アローラのすがた"}}

    def test_create_regional_variant_param_none(self) -> None:
        p = param.CreateRegionalVariantParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateMegaEvolutionParam:
    def test_create_mega_evolution_param_false(self) -> None:
        p = param.CreateMegaEvolutionParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_mega_evolution": False}}

    def test_create_mega_evolution_param_true(self) -> None:
        p = param.CreateMegaEvolutionParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_mega_evolution": True}}

    def test_create_regional_variant_param_none(self) -> None:
        p = param.CreateMegaEvolutionParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreatePrimalReversionParam:
    def test_create_primal_reversion_param_false(self) -> None:
        p = param.CreatePrimalReversionParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_primal_reversion": False}}

    def test_create_primal_reversion_param_true(self) -> None:
        p = param.CreatePrimalReversionParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_primal_reversion": True}}

    def test_create_primal_reversion_param_none(self) -> None:
        p = param.CreatePrimalReversionParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateLegendaryParam:
    def test_create_legendary_param_false(self) -> None:
        p = param.CreateLegendaryParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_legendary": False}}

    def test_create_legendary_param_true(self) -> None:
        p = param.CreateLegendaryParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_legendary": True}}

    def test_create_legendary_param_none(self) -> None:
        p = param.CreateLegendaryParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateMythicalParam:
    def test_create_mythical_param_false(self) -> None:
        p = param.CreateMythicalParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_mythical": False}}

    def test_create_mythical_param_true(self) -> None:
        p = param.CreateMythicalParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_mythical": True}}

    def test_create_mythical_param_none(self) -> None:
        p = param.CreateMythicalParam(None)
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateGenderTypeParam:
    def test_create_gender_type_param_0_0(self) -> None:
        p = param.CreateGenderTypeParam(("0", "0"))
        actual = p.create_param()

        assert actual == [
            {"term": {"gender_type.has_male": False}},
            {"term": {"gender_type.has_female": False}},
        ]

    def test_create_gender_type_param_0_1(self) -> None:
        p = param.CreateGenderTypeParam(("0", "1"))
        actual = p.create_param()

        assert actual == [
            {"term": {"gender_type.has_male": False}},
            {"term": {"gender_type.has_female": True}},
        ]

    def test_create_gender_type_param_1_0(self) -> None:
        p = param.CreateGenderTypeParam(("1", "0"))
        actual = p.create_param()

        assert actual == [
            {"term": {"gender_type.has_male": True}},
            {"term": {"gender_type.has_female": False}},
        ]

    def test_create_gender_type_param_1_1(self) -> None:
        p = param.CreateGenderTypeParam(("1", "1"))
        actual = p.create_param()

        assert actual == [
            {"term": {"gender_type.has_male": True}},
            {"term": {"gender_type.has_female": True}},
        ]

    def test_create_gender_type_param_none(self) -> None:
        p = param.CreateGenderTypeParam((None, None))
        actual = p.create_param()

        assert actual is None

    def test_create_gender_type_param_invalid(self) -> None:
        p = param.CreateGenderTypeParam(("foo", "bar"))
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreatePokemonTypeParam:
    def test_create_pokemon_type_param_1_0(self) -> None:
        p = param.CreatePokemonTypeParam(("ほのお", None))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "ほのお",
                    "fields": [
                        "pokemon_type.type_1.keyword",
                        "pokemon_type.type_2.keyword",
                    ],
                }
            }
        ]

    def test_create_pokemon_type_param_1_1(self) -> None:
        p = param.CreatePokemonTypeParam(("ほのお", "ひこう"))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "ほのお",
                    "fields": [
                        "pokemon_type.type_1.keyword",
                        "pokemon_type.type_2.keyword",
                    ],
                }
            },
            {
                "multi_match": {
                    "query": "ひこう",
                    "fields": [
                        "pokemon_type.type_1.keyword",
                        "pokemon_type.type_2.keyword",
                    ],
                }
            },
        ]

    def test_create_pokemon_type_param_0_1(self) -> None:
        p = param.CreatePokemonTypeParam((None, "ひこう"))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "ひこう",
                    "fields": [
                        "pokemon_type.type_1.keyword",
                        "pokemon_type.type_2.keyword",
                    ],
                }
            }
        ]

    def test_create_pokemon_type_param_none(self) -> None:
        p = param.CreatePokemonTypeParam((None, None))
        actual = p.create_param()

        assert actual is None


@pytest.mark.param()
class TestCreateAbilityParam:
    def test_create_ability_param_1_0_0(self) -> None:
        p = param.CreateAbilityParam(("にげあし", None, None))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "にげあし",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            }
        ]

    def test_create_ability_param_1_1_0(self) -> None:
        p = param.CreateAbilityParam(("にげあし", "するどいめ", None))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "にげあし",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
            {
                "multi_match": {
                    "query": "するどいめ",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
        ]

    def test_create_ability_param_1_1_1(self) -> None:
        p = param.CreateAbilityParam(("にげあし", "するどいめ", "おみとおし"))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "にげあし",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
            {
                "multi_match": {
                    "query": "するどいめ",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
            {
                "multi_match": {
                    "query": "おみとおし",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
        ]

    def test_create_ability_param_0_1_0(self) -> None:
        p = param.CreateAbilityParam((None, "するどいめ", None))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "するどいめ",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            }
        ]

    def test_create_ability_param_0_1_1(self) -> None:
        p = param.CreateAbilityParam((None, "するどいめ", "おみとおし"))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "するどいめ",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
            {
                "multi_match": {
                    "query": "おみとおし",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            },
        ]

    def test_create_ability_param_0_0_1(self) -> None:
        p = param.CreateAbilityParam((None, None, "おみとおし"))
        actual = p.create_param()

        assert actual == [
            {
                "multi_match": {
                    "query": "おみとおし",
                    "fields": [
                        "abilities.ability_1.keyword",
                        "abilities.ability_2.keyword",
                        "abilities.hidden_ability.keyword",
                    ],
                }
            }
        ]

    def test_create_ability_param_none(self) -> None:
        p = param.CreateAbilityParam((None, None, None))
        actual = p.create_param()

        assert actual is None
