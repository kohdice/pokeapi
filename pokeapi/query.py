from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Param(ABC):
    @abstractmethod
    def create_param(self) -> dict[str, Any] | None:
        pass


@dataclass
class CreatePokedexNumberParam(Param):
    pokedex_number: str | None

    def create_param(self) -> dict[str, Any] | None:
        if self.pokedex_number is None:
            return None
        try:
            pokedex_number = int(self.pokedex_number)
        except ValueError:
            return None

        return {"term": {"national_pokedex_number": {"value": pokedex_number}}}
