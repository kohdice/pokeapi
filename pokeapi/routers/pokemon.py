import random
from typing import Annotated

from fastapi import APIRouter, Path, Query

from ..schemas.pokemon import Pokemon
from ..search import accessor
from ..search.query import CreatePokedexNumberQuery, CreatePokemonNameQuery

router = APIRouter()


@router.get("/pokemon", response_model=list[Pokemon])
async def read_pokemon() -> list[Pokemon]:
    # Numbers for all ranges of National Pokédex Number.
    # But not supported by data for testing.

    # query = CreatePokedexNumberQuery().create_query(random.randint(1, 1014))

    # Numbers corresponding to the data for testing.
    test_numbers = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        25,
        26,
        150,
        151,
        161,
        162,
        382,
        383,
        778,
    ]

    query = CreatePokedexNumberQuery().create_query(
        random.choice(test_numbers)
    )
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)


@router.get("/pokemon/name/{name}", response_model=list[Pokemon])
async def read_pokemon_by_name(
    name: Annotated[str, Query(title="Pokémon Name of Pokémon to get")]
) -> list[Pokemon]:
    query = CreatePokemonNameQuery().create_query(name)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)


@router.get(
    "/pokemon/pokedex_number/{pokedex_number}",
    response_model=list[Pokemon],
)
async def read_pokemon_by_pokedex_number(
    pokedex_number: Annotated[
        int,
        Path(title="National Pokédex Number of Pokémon to get", gt=1, le=1015),
    ]
) -> list[Pokemon]:
    query = CreatePokedexNumberQuery().create_query(pokedex_number)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)


@router.get("/pokemon/conditions")
async def read_pokemon_by_conditions(
    condition: str | int,
) -> dict[str, int | str]:
    return {
        "national_pokedex_number": 152,
        "name": "けつばん",
        "condition": condition,
    }
