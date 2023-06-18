from fastapi import APIRouter

router = APIRouter()


@router.get("/pokemon")
async def read_pokemon() -> dict[str, str]:
    return {"Name": "けつばん"}


@router.get("/pokemon/name/{name}")
async def read_pokemon_by_name(name: str) -> dict[str, str]:
    return {"Name": name}
