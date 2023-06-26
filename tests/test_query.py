import pytest

from pokeapi.search import param, query


@pytest.mark.query()
class TestCreateNationalPokedexNumberQuery:
    def test_create_query(self) -> None:
        q = query.CreatePokedexNumberQuery()
        actual = q.create_query(1)

        assert actual == {
            "query": {
                "bool": {"must": [{"term": {"national_pokedex_number": 1}}]}
            }
        }


@pytest.mark.query()
class TestCreatePokemonNameQuery:
    def test_create_query(self) -> None:
        q = query.CreatePokemonNameQuery()
        actual = q.create_query("フシギダネ")

        assert actual == {
            "query": {"bool": {"must": [{"term": {"name": "フシギダネ"}}]}}
        }


@pytest.mark.query()
class TestCreateConditionalSearchQuery:
    def test_create_query_form(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreateFormParam("れいじゅうフォルム"),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {"must": [{"term": {"form.keyword": "れいじゅうフォルム"}}]}
            }
        }

    def test_create_query_regional_variant(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreateRegionalVariantParam("アローラのすがた"),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"regional_variant.keyword": "アローラのすがた"}}
                    ]
                }
            }
        }

    def test_create_query_mega_evolution(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreateMegaEvolutionParam(True),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {"must": [{"term": {"is_mega_evolution": True}}]}
            }
        }

    def test_create_query_primal_reversion(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreatePrimalReversionParam(True),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {"must": [{"term": {"is_primal_reversion": True}}]}
            }
        }

    def test_create_query_legendary(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreateLegendaryParam(True),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {"bool": {"must": [{"term": {"is_legendary": True}}]}}
        }

    def test_create_query_mythical(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreateMythicalParam(True),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {"bool": {"must": [{"term": {"is_mythical": True}}]}}
        }

    def test_create_query_gender_type(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (
            param.CreateGenderTypeParam((True, "hoge")),  # type: ignore
        )
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"gender_type.has_male": True}},
                    ]
                }
            }
        }

    def test_create_query_pokemon_type(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreatePokemonTypeParam(("ほのお", None)),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": "ほのお",
                                "fields": [
                                    "pokemon_type.type_1.keyword",
                                    "pokemon_type.type_2.keyword",
                                ],
                            }
                        },
                    ]
                }
            }
        }

    def test_create_query_ability(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (param.CreateAbilityParam(("もうか", None, "サンパワー")),)
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": "もうか",
                                "fields": [
                                    "abilities.ability_1.keyword",
                                    "abilities.ability_2.keyword",
                                    "abilities.hidden_ability.keyword",
                                ],
                            }
                        },
                        {
                            "multi_match": {
                                "query": "サンパワー",
                                "fields": [
                                    "abilities.ability_1.keyword",
                                    "abilities.ability_2.keyword",
                                    "abilities.hidden_ability.keyword",
                                ],
                            }
                        },
                    ]
                }
            }
        }

    def test_create_query_multiple_conditions(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (
            param.CreateFormParam("れいじゅうフォルム"),
            param.CreatePokemonTypeParam(("ほのお", None)),
        )
        actual = q.create_query(conditions)

        assert actual == {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"form.keyword": "れいじゅうフォルム"}},
                        {
                            "multi_match": {
                                "query": "ほのお",
                                "fields": [
                                    "pokemon_type.type_1.keyword",
                                    "pokemon_type.type_2.keyword",
                                ],
                            }
                        },
                    ]
                }
            }
        }

    def test_create_query_none(self) -> None:
        q = query.CreateConditionalSearchQuery()
        conditions = (
            param.CreateFormParam(None),
            param.CreateRegionalVariantParam(None),
        )
        actual = q.create_query(conditions)

        assert actual == {"query": {"bool": {"must": []}}}


class TestCreateKeywordQuery:
    def test_create_query(self) -> None:
        q = query.CreateKeywordQuery()
        actual = q.create_query("アローラ")

        assert actual == {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": "アローラ",
                                "operator": "and",
                                "fields": [
                                    "abilities.ability_1",
                                    "abilities.ability_2",
                                    "abilities.hidden_ability",
                                    "form",
                                    "name",
                                    "pokemon_type.type_1",
                                    "pokemon_type.type_2",
                                    "regional_variant",
                                ],
                            }
                        }
                    ]
                }
            }
        }
