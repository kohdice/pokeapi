import pytest

from pokeapi import query


@pytest.mark.query()
class TestCreatePokemonNameQuery:
    def test_create_query(self) -> None:
        q = query.CreatePokemonNameQuery()
        actual = q.create_query("フシギダネ")

        assert actual == {
            "query": {"bool": {"must": {"term": {"name": "フシギダネ"}}}}
        }

    def test_create_query_none(self) -> None:
        q = query.CreatePokemonNameQuery()
        actual = q.create_query(None)

        assert actual is None
