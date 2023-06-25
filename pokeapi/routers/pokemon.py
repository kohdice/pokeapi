from typing import Annotated

from fastapi import APIRouter, Path, Query

from ..schemas.pokemon import Pokemon
from ..search import accessor
from ..search.query import CreatePokedexNumberQuery, CreatePokemonNameQuery

router = APIRouter()


@router.get("/pokemon")
async def read_pokemon() -> dict[str, str]:
    return {"name": "けつばん"}


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
