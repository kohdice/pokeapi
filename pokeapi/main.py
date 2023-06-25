from fastapi import FastAPI

from .routers import pokemon_router

app = FastAPI()
app.include_router(pokemon_router.router)


@app.get("/")
def read_root() -> dict:
    return {"Prof. Oak": "Welcome to Pokédex!"}
