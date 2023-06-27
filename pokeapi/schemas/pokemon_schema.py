from pydantic import BaseModel


class PokemonSchema(BaseModel):
    """Response schema class for Pokémon."""

    national_pokedex_number: int
    name: str
    form: str | None
    regional_variant: str | None
    is_mega_evolution: bool
    is_primal_reversion: bool
    is_legendary: bool
    is_mythical: bool
    height: float
    weight: float
    gender_type: dict
    pokemon_type: dict
    abilities: dict
    base_stats: dict
