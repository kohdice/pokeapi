from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"Message": "Welcome to Pokédex!"}


@app.get("/pokemon/{national_pokedex_number}")
def read_pokemon(national_pokedex_number: int) -> dict:
    return {
        "National Pokédex Number": national_pokedex_number,
        "Name": "けつばん",
    }
