from typing import Any, Generator

from elasticsearch import Elasticsearch

from ..schemas.pokemon_schema import PokemonSchema
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
        response = es.search(index=conf.ES_INDEX, body=query)

    for doc in response["hits"]["hits"]:
        yield doc["_source"]


def create_pokemon_response(
    es_response: Generator[dict, None, None]
) -> list[PokemonSchema]:
    """Method to create a response to Pokémon schema.

    Args:
        es_response (Generator): Generator of Pokémon data
        read from elasticsearch.

    Returns:
        list[Pokemon]: List with Pokémon information.

    """

    response: list[PokemonSchema] = []
    for doc in es_response:
        response.append(
            PokemonSchema(
                national_pokedex_number=doc["national_pokedex_number"],
                name=doc["name"],
                form=doc["form"],
                regional_variant=doc["regional_variant"],
                is_mega_evolution=doc["is_mega_evolution"],
                is_primal_reversion=doc["is_primal_reversion"],
                is_legendary=doc["is_legendary"],
                is_mythical=doc["is_mythical"],
                height=doc["height"],
                weight=doc["weight"],
                gender_type=doc["gender_type"],
                pokemon_type=doc["pokemon_type"],
                abilities=doc["abilities"],
                base_stats=doc["base_stats"],
            )
        )

    return response
