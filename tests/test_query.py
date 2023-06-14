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
