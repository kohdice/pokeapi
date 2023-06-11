import os
from typing import Generator

import pytest


@pytest.fixture()
def _setup_get_config() -> Generator[None, None, None]:
    os.environ["ES_INDEX"] = "pokemon"
    os.environ["ES_CONNECTION_URL"] = "http://elasticsearch_test:9200"
    yield
    del os.environ["ES_INDEX"]
    del os.environ["ES_CONNECTION_URL"]
