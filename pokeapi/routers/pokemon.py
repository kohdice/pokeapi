from fastapi import APIRouter

router = APIRouter()


@router.get("/pokemon")
async def read_pokemon() -> dict[str, str]:
    return {"name": "けつばん"}


@router.get("/pokemon/name/{name}")
async def read_pokemon_by_name(name: str) -> dict[str, str]:
    return {"name": name}


@router.get("/pokemon/pokedex_number/{pokedex_number}")
async def read_pokemon_by_pokedex_number(
    pokedex_number: int,
) -> dict[str, int | str]:
    return {"national_pokedex_number": pokedex_number, "name": "けつばん"}
