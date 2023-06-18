from fastapi import FastAPI

from .routers import pokemon

app = FastAPI()
app.include_router(pokemon.router)


@app.get("/")
def read_root() -> dict:
    return {"Prof. Oak": "Welcome to Pokédex!"}
