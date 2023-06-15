from typing import Any

import pytest

from pokeapi import query


class TestAbstractParam:
    class SubParam(query.Param):
        def create_param(self) -> dict[str, Any] | None:
            return None

    class ErrorSubParam(query.Param):
        pass

    def test_create_param(self) -> None:
        p = self.SubParam()
        actual = p.create_param()

        assert actual is None

    def test_not_implemented(self) -> None:
        with pytest.raises(TypeError):
            self.ErrorSubParam()


class TestCreatePokedexNumberParam:
    def test_create_pokedex_number_param(self) -> None:
        q = query.CreatePokedexNumberParam("1")
        actual = q.create_param()

        assert actual == {"term": {"national_pokedex_number": {"value": 1}}}

    def test_create_pokedex_number_param_not_number(self) -> None:
        q = query.CreatePokedexNumberParam("test")
        actual = q.create_param()

        assert actual is None

    def test_create_pokedex_number_param_none(self) -> None:
        q = query.CreatePokedexNumberParam(None)
        actual = q.create_param()

        assert actual is None


class TestCreateNameParam:
    def test_create_name_param(self) -> None:
        p = query.CreateNameParam("フシギダネ")
        actual = p.create_param()

        assert actual == {"term": {"name": {"value": "フシギダネ"}}}

    def test_create_name_param_none(self) -> None:
        p = query.CreateNameParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreateformParam:
    def test_create_form_param(self) -> None:
        p = query.CreateFormParam("れいじゅうフォルム")
        actual = p.create_param()

        assert actual == {"term": {"form": {"value": "れいじゅうフォルム"}}}

    def test_create_form_param_none(self) -> None:
        p = query.CreateFormParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreateRegionalVariantParam:
    def test_create_regional_variant_param(self) -> None:
        p = query.CreateRegionalVariantParam("アローラのすがた")
        actual = p.create_param()

        assert actual == {"term": {"regional_variant": {"value": "アローラのすがた"}}}

    def test_create_regional_variant_param_none(self) -> None:
        p = query.CreateRegionalVariantParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreateMegaEvolutionParam:
    def test_create_mega_evolution_param_false(self) -> None:
        p = query.CreateMegaEvolutionParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_mega_evolution": {"value": False}}}

    def test_create_mega_evolution_param_true(self) -> None:
        p = query.CreateMegaEvolutionParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_mega_evolution": {"value": True}}}

    def test_create_regional_variant_param_none(self) -> None:
        p = query.CreateMegaEvolutionParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreatePrimalReversionParam:
    def test_create_primal_reversion_param_false(self) -> None:
        p = query.CreatePrimalReversionParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_primal_reversion": {"value": False}}}

    def test_create_primal_reversion_param_true(self) -> None:
        p = query.CreatePrimalReversionParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_primal_reversion": {"value": True}}}

    def test_create_primal_reversion_param_none(self) -> None:
        p = query.CreatePrimalReversionParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreateLegendaryParam:
    def test_create_legendary_param_false(self) -> None:
        p = query.CreateLegendaryParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_legendary": {"value": False}}}

    def test_create_legendary_param_true(self) -> None:
        p = query.CreateLegendaryParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_legendary": {"value": True}}}

    def test_create_legendary_param_none(self) -> None:
        p = query.CreateLegendaryParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreateMythicalParam:
    def test_create_mythical_param_false(self) -> None:
        p = query.CreateMythicalParam("0")
        actual = p.create_param()

        assert actual == {"term": {"is_mythical": {"value": False}}}

    def test_create_mythical_param_true(self) -> None:
        p = query.CreateMythicalParam("1")
        actual = p.create_param()

        assert actual == {"term": {"is_mythical": {"value": True}}}

    def test_create_mythical_param_none(self) -> None:
        p = query.CreateMythicalParam(None)
        actual = p.create_param()

        assert actual is None


class TestCreateGenderTypeParam:
    def test_create_gender_type_param_0_0(self) -> None:
        p = query.CreateGenderTypeParam(("0", "0"))
        actual = p.create_param()

        assert actual == [
            {"match": {"gender_type.has_male": False}},
            {"match": {"gender_type.has_female": False}},
        ]

    def test_create_gender_type_param_0_1(self) -> None:
        p = query.CreateGenderTypeParam(("0", "1"))
        actual = p.create_param()

        assert actual == [
            {"match": {"gender_type.has_male": False}},
            {"match": {"gender_type.has_female": True}},
        ]

    def test_create_gender_type_param_1_0(self) -> None:
        p = query.CreateGenderTypeParam(("1", "0"))
        actual = p.create_param()

        assert actual == [
            {"match": {"gender_type.has_male": True}},
            {"match": {"gender_type.has_female": False}},
        ]

    def test_create_gender_type_param_1_1(self) -> None:
        p = query.CreateGenderTypeParam(("1", "1"))
        actual = p.create_param()

        assert actual == [
            {"match": {"gender_type.has_male": True}},
            {"match": {"gender_type.has_female": True}},
        ]

    def test_create_gender_type_param_none(self) -> None:
        p = query.CreateGenderTypeParam((None, None))
        actual = p.create_param()

        assert actual is None

    def test_create_gender_type_param_invalid(self) -> None:
        p = query.CreateGenderTypeParam(("foo", "bar"))
        actual = p.create_param()

        assert actual is None
