import random
from typing import Annotated

from fastapi import APIRouter, Path, Query

from pokeapi.search.param import (
    CreateAbilityParam,
    CreateFormParam,
    CreateGenderTypeParam,
    CreateLegendaryParam,
    CreateMegaEvolutionParam,
    CreateMythicalParam,
    CreatePokemonTypeParam,
    CreatePrimalReversionParam,
    CreateRegionalVariantParam,
)

from ..schemas.pokemon_schema import PokemonSchema
from ..search import accessor
from ..search.query import (
    CreateConditionalSearchQuery,
    CreatePokedexNumberQuery,
    CreatePokemonNameQuery,
)

router = APIRouter()


@router.get("/pokemon", response_model=list[PokemonSchema])
async def read_pokemon() -> list[PokemonSchema]:
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


@router.get("/pokemon/name/{name}", response_model=list[PokemonSchema])
async def read_pokemon_by_name(
    name: Annotated[str, Query(title="Pokémon Name of Pokémon to get")]
) -> list[PokemonSchema]:
    query = CreatePokemonNameQuery().create_query(name)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)


@router.get(
    "/pokemon/pokedex_number/{pokedex_number}",
    response_model=list[PokemonSchema],
)
async def read_pokemon_by_pokedex_number(
    pokedex_number: Annotated[
        int,
        Path(title="National Pokédex Number of Pokémon to get", gt=1, le=1015),
    ]
) -> list[PokemonSchema]:
    query = CreatePokedexNumberQuery().create_query(pokedex_number)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)


@router.get(
    "/pokemon/conditions", response_model=list[PokemonSchema] | dict[str, str]
)
async def read_pokemon_by_conditions(
    ability_1: str | None = None,
    ability_2: str | None = None,
    hidden_ability: str | None = None,
    form: str | None = None,
    has_male: bool | None = None,
    has_female: bool | None = None,
    is_legendary: bool | None = None,
    is_mega_evolution: bool | None = None,
    is_mythical: bool | None = None,
    type_1: str | None = None,
    type_2: str | None = None,
    is_primal_reversion: bool | None = None,
    regional_variant: str | None = None,
) -> list[PokemonSchema] | dict[str, str]:
    request_params = (
        CreateAbilityParam((ability_1, ability_2, hidden_ability)),
        CreateFormParam(form),
        CreateGenderTypeParam((has_male, has_female)),
        CreateLegendaryParam(is_legendary),
        CreateMegaEvolutionParam(is_mega_evolution),
        CreateMythicalParam(is_mythical),
        CreatePokemonTypeParam((type_1, type_2)),
        CreatePrimalReversionParam(is_primal_reversion),
        CreateRegionalVariantParam(regional_variant),
    )

    query = CreateConditionalSearchQuery().create_query(request_params)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)
