from dataclasses import FrozenInstanceError

import pytest

from pokeapi.search import config
from pokeapi.search.config import Singleton


class TestSingleton:
    class SingletonTestClass(metaclass=Singleton):
        pass

    def test_singleton(self) -> None:
        assert self.SingletonTestClass() is self.SingletonTestClass()


class TestConfig:
    @pytest.mark.usefixtures("_setup_get_config")
    def test_get_config(self) -> None:
        actual = config.get_config()

        assert actual.ES_INDEX == "pokemon"
        assert actual.ES_CONNECTION_URL == "http://elasticsearch_test:9200"

        actual_clone = config.get_config()
        assert actual is actual_clone

        with pytest.raises(FrozenInstanceError) as index_e:
            actual.ES_INDEX = "hoge"

        assert str(index_e.value) == "cannot assign to field 'ES_INDEX'"

        with pytest.raises(FrozenInstanceError) as url_e:
            actual.ES_CONNECTION_URL = "hoge"

        assert str(url_e.value) == "cannot assign to field 'ES_CONNECTION_URL'"
