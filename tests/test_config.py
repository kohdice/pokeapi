import pytest

from pokeapi.search import config
from pokeapi.search.config import Singleton, StageEnvIsWorngException


class TestSingleton:
    class SingletonTestClass(metaclass=Singleton):
        pass

    def test_singleton(self) -> None:
        assert self.SingletonTestClass() is self.SingletonTestClass()


class TestConfig:
    def test_get_config_worng(self, env_wrong) -> None:
        with pytest.raises(StageEnvIsWorngException) as e:
            config.get_config()

        assert str(e.value) == "STAGE=hogehoge is an invalid value."

    def test_get_config_development(self, env_development) -> None:
        actual = config.get_config()

        assert actual.ES_INDEX == "pokemon"
        assert actual.ES_CONNECTION == "http://elasticsearch:9200"

    def test_get_config_staging(self, env_staging) -> None:
        actual = config.get_config()

        assert actual.ES_INDEX == "pokemon"
        assert actual.ES_CONNECTION == "http://elasticsearch_staging:9200"

    def test_get_config_production(self, env_production) -> None:
        actual = config.get_config()

        assert actual.ES_INDEX == "pokemon"
        assert actual.ES_CONNECTION == "http://elasticsearch_production:9200"
