import os
from dataclasses import FrozenInstanceError
from typing import Generator

import pytest

from pokeapi.search import config
from pokeapi.search.config import Singleton


def dynamic_connection_url() -> Generator[str, None, None]:
    if os.getenv("STAGE") == "development":
        yield "http://elasticsearch:9200"
    else:
        yield "http://localhost:9200"


class TestSingleton:
    class SingletonTestClass(metaclass=Singleton):
        pass

    def test_singleton(self) -> None:
        assert self.SingletonTestClass() is self.SingletonTestClass()


class TestConfig:
    @pytest.mark.usefixtures("_setup_get_config")
    @pytest.mark.parametrize("expected", dynamic_connection_url())
    def test_get_config(self, expected) -> None:
        actual = config.get_config()

        assert actual.ES_INDEX == "pokemon"
        assert actual.ES_CONNECTION_URL == expected

        actual_clone = config.get_config()
        assert actual is actual_clone

        with pytest.raises(FrozenInstanceError) as index_e:
            actual.ES_INDEX = "hoge"

        assert str(index_e.value) == "cannot assign to field 'ES_INDEX'"

        with pytest.raises(FrozenInstanceError) as url_e:
            actual.ES_CONNECTION_URL = "hoge"

        assert str(url_e.value) == "cannot assign to field 'ES_CONNECTION_URL'"
