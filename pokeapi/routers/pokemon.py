from fastapi import APIRouter

router = APIRouter()


@router.get("/pokemon")
async def read_pokemon() -> dict[str, str]:
    return {"Name": "けつばん"}
