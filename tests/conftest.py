import os

import pytest


@pytest.fixture
def env_wrong():
    os.environ["STAGE"] = "hogehoge"
    yield
    del os.environ["STAGE"]


@pytest.fixture
def env_development():
    os.environ["STAGE"] = "development"
    yield
    del os.environ["STAGE"]


@pytest.fixture
def env_staging():
    os.environ["STAGE"] = "staging"
    os.environ["ES_CONNECTION_STAGING"] = "http://elasticsearch_staging:9200"
    yield
    del os.environ["STAGE"]
    del os.environ["ES_CONNECTION_STAGING"]


@pytest.fixture
def env_production():
    os.environ["STAGE"] = "production"
    os.environ[
        "ES_CONNECTION_PRODUCTION"
    ] = "http://elasticsearch_production:9200"
    yield
    del os.environ["STAGE"]
    del os.environ["ES_CONNECTION_PRODUCTION"]
