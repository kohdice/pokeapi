from typing import Any, Generator

from elasticsearch import Elasticsearch

from . import config


def search_pokemon(query: dict[str, Any]) -> Generator[dict, None, None]:
    """Method to connect to elasticsearch and search for Pokémon.

    Args:
        query (dict): Query to search for Pokémon.

    Yields:
        dict[str, Any]: Dict with Pokémon information.

    """

    conf = config.get_config()
    with Elasticsearch(
        conf.ES_CONNECTION_URL, http_compress=True, timeout=10
    ) as es:
        responce = es.search(index=conf.ES_INDEX, body=query)

    for doc in responce["hits"]["hits"]:
        yield doc["_source"]
