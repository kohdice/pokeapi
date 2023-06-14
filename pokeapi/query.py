from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Param(ABC):
    """Abstract class for parameter creation"""

    @abstractmethod
    def create_param(self) -> dict[str, Any] | None:
        """Abstract method for parameter creation

        Returns:
            dict[str, Any] | None:
            Dict with search parameters for elasticsearch
        """
        pass


@dataclass
class CreatePokedexNumberParam(Param):
    """Dataclass to create search parameters for `National Pokédex Number`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    pokedex_number: str | None

    def create_param(self) -> dict[str, Any] | None:
        """Method to create search parameters of `National Pokédex Number`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `National Pokémon Number`
            for elasticsearch
        """
        if self.pokedex_number is None:
            return None
        try:
            pokedex_number = int(self.pokedex_number)
        except ValueError:
            return None

        return {"term": {"national_pokedex_number": {"value": pokedex_number}}}


@dataclass
class CreateNameParam(Param):
    """Dataclass to create search parameters for `Name of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    name: str | None

    def create_param(self) -> dict[str, Any] | None:
        """Method to create search parameters of `Name of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Name of Pokémon`for elasticsearch
        """
        if self.name is None:
            return None
        return {"term": {"name": {"value": self.name}}}


@dataclass
class CreateFormParam(Param):
    """Dataclass to create search parameters of `Form of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    form: str | None

    def create_param(self) -> dict[str, Any] | None:
        """Method to create search parameters of `Form of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Form of Pokémon`for elasticsearch
        """
        if self.form is None:
            return None
        return {"term": {"form": {"value": self.form}}}


@dataclass
class CreateRegionalVariantParam(Param):
    """Dataclass to create search parameters of `Regional Variant of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    regional_variant: str | None

    def create_param(self) -> dict[str, Any] | None:
        """Method to create search parameters of `Regional Variant of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Regional Variant of Pokémon`
            for elasticsearch
        """
        if self.regional_variant is None:
            return None
        return {"term": {"regional_variant": {"value": self.regional_variant}}}
