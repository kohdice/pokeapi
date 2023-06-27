from fastapi import FastAPI

from .routers import pokemon_router
from .schemas.message_schema import RootMessageSchema

app = FastAPI()
app.include_router(pokemon_router.router)


@app.get("/", response_model=RootMessageSchema)
def read_root() -> RootMessageSchema:
    """Path operation function for root endpoint.

    Returns:
        RootMessageSchema: Object for response of root endpoint.

    """

    return RootMessageSchema(message="Welcome to Pokédex!")
