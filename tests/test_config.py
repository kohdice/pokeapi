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
    def test_get_config(self, expected: str) -> None:
        actual = config.get_config()

        assert actual.ES_INDEX == "pokemon"
        assert actual.ES_CONNECTION_URL == expected

        actual_clone = config.get_config()
        assert actual is actual_clone

        with pytest.raises(FrozenInstanceError):
            actual.ES_INDEX = "hoge"  # type: ignore

        with pytest.raises(FrozenInstanceError):
            actual.ES_CONNECTION_URL = "hoge"  # type: ignore
