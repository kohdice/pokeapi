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
    CreateKeywordQuery,
    CreatePokedexNumberQuery,
    CreatePokemonNameQuery,
)

router = APIRouter()


@router.get("/pokemon", response_model=list[PokemonSchema])
async def read_pokemon() -> list[PokemonSchema]:
    """Path operation function for /pokemon endpoint.

    Returns:
        list[PokemonSchema]: List containing Pokémon data..

    """

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
    """Path operation function for /pokemon/name endpoint.

    Args:
        name (str): Target of `name`.

    Returns:
        list[PokemonSchema]: List containing Pokémon data.

    """

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
    """Path operation function for /pokemon/pokedex_number endpoint.

    Args:
        pokedex_number (int): Target of `national_pokédex_number`.

    Returns:
        list[PokemonSchema]: List containing Pokémon data.

    """

    query = CreatePokedexNumberQuery().create_query(pokedex_number)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)


@router.get("/pokemon/conditions", response_model=list[PokemonSchema])
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
) -> list[PokemonSchema]:
    """Path operation function for /pokemon/conditions endpoint.

    Args:
        ability_1 (str): Target of `ability_1`.
        ability_2 (str): Target of `ability_2`.
        hidden_ability (str): Target of `hidden_ability`.
        form (str): Target of `form`.
        has_male (bool): Target of `has_male`.
        has_female (bool): Target of `has_female`.
        is_legendary (bool): Target of `is_legendary`.
        is_mega_evolution (bool): Target of `is_mega_evolution`.
        is_mythical (bool): Target of `is_mythical`.
        type_1 (str): Target of `type_1`.
        type_2 (str): Target of `type_2`.
        is_primal_reversion (bool): Target of `is_primal_reversion`.
        regional_variant (bool): Target of `regional_variant`.

    Returns:
        list[PokemonSchema]: List containing Pokémon data.

    """

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


@router.get("/pokemon/keyword/{keyword}", response_model=list[PokemonSchema])
async def read_pokemon_by_keyword(
    keyword: Annotated[str, Query(title="Keyword of Pokémon to get")]
) -> list[PokemonSchema]:
    """Path operation function for /pokemon/keyword endpoint.

    Args:
        keyword (str): Keyword for searching Pokémon.

    Returns:
        list[PokemonSchema]: List containing Pokémon data.

    """

    query = CreateKeywordQuery().create_query(keyword)
    es_response = accessor.search_pokemon(query)

    return accessor.create_pokemon_response(es_response)
