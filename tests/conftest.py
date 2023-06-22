import os
from typing import Generator

import pytest


@pytest.fixture()
def _setup_get_config() -> Generator[None, None, None]:
    url = "http://localhost:9200"

    if os.getenv("STAGE") == "development":
        url = "http://elasticsearch:9200"

    os.environ["ES_INDEX"] = "pokemon"
    os.environ["ES_CONNECTION_URL"] = url
    yield
    del os.environ["ES_INDEX"]
    del os.environ["ES_CONNECTION_URL"]
