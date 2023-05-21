from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}


@app.get("/pokemon/{pokemon}")
def read_pokemon(pokemon: int, q: Union[str, None] = None) -> dict:
    return {"pokemon": pokemon, "q": q}
