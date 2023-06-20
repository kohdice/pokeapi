from typing import Any

from elasticsearch import Elasticsearch

from . import config


def search_pokemon(query: dict[str, Any]) -> list[dict]:
    """Method to connect to elasticsearch and search for Pokémon.

    Args:
        query (dict): Query to search for Pokémon.

    Returns:
        list[dict]: List with information on Pokémon.

    """

    conf = config.get_config()
    with Elasticsearch(
        conf.ES_CONNECTION_URL, http_compress=True, timeout=10
    ) as es:
        responce = es.search(index=conf.ES_INDEX, body=query)
        pokemon_list: list[dict] = []
        for doc in responce["hits"]["hits"]:
            pokemon_list.append(doc["_source"])

    return pokemon_list
