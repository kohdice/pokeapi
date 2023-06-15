from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Param(ABC):
    """Abstract class for parameter creation"""

    @abstractmethod
    def create_param(self) -> dict[str, Any] | None:
        """Abstract method for parameter creation"""
        pass


@dataclass
class CreatePokedexNumberParam(Param):
    """Dataclass to create search parameters for `National Pokédex Number`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    pokedex_number: str | None

    def create_param(self) -> dict[str, dict[str, dict[str, int]]] | None:
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

    def create_param(self) -> dict[str, dict[str, dict[str, Any]]] | None:
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

    def create_param(self) -> dict[str, dict[str, dict[str, Any]]] | None:
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

    def create_param(self) -> dict[str, dict[str, dict[str, Any]]] | None:
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


@dataclass
class CreateMegaEvolutionParam(Param):
    """Dataclass to create search parameters of `Mega Evolution of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_mega_evolution: str | None

    def create_param(self) -> dict[str, dict[str, dict[str, bool]]] | None:
        """Method to create search parameters of `Mega Evolution of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Mega Evolution of Pokémon`
            for elasticsearch
        """
        match self.is_mega_evolution:
            case "0":
                return {"term": {"is_mega_evolution": {"value": False}}}
            case "1":
                return {"term": {"is_mega_evolution": {"value": True}}}
            case _:
                return None


@dataclass
class CreatePrimalReversionParam(Param):
    """Dataclass to create search parameters of `Primal Reversion of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_primal_reversion: str | None

    def create_param(self) -> dict[str, dict[str, dict[str, bool]]] | None:
        """Method to create search parameters of `Primal Reversion of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Primal Reversion of Pokémon`
            for elasticsearch
        """
        match self.is_primal_reversion:
            case "0":
                return {"term": {"is_primal_reversion": {"value": False}}}
            case "1":
                return {"term": {"is_primal_reversion": {"value": True}}}
            case _:
                return None


@dataclass
class CreateLegendaryParam(Param):
    """Dataclass to create search parameters of `Legendary of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_legendary: str | None

    def create_param(self) -> dict[str, dict[str, dict[str, bool]]] | None:
        """Method to create search parameters of `Legendary of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Legendary of Pokémon`
            for elasticsearch
        """
        match self.is_legendary:
            case "0":
                return {"term": {"is_legendary": {"value": False}}}
            case "1":
                return {"term": {"is_legendary": {"value": True}}}
            case _:
                return None


@dataclass
class CreateMythicalParam(Param):
    """Dataclass to create search parameters of `Mythical of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_mythical: str | None

    def create_param(self) -> dict[str, dict[str, dict[str, bool]]] | None:
        """Method to create search parameters of `Mythical of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, Any] | None:
            Dict with search parameters of `Mythical of Pokémon`
            for elasticsearch
        """
        match self.is_mythical:
            case "0":
                return {"term": {"is_mythical": {"value": False}}}
            case "1":
                return {"term": {"is_mythical": {"value": True}}}
            case _:
                return None


@dataclass
class CreateGenderTypeParam(Param):
    """Dataclass to create search parameters of `Gender Type of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    gender_type: tuple[str | None, ...]

    def create_param(self) -> list[dict[str, dict[str, bool]]] | None:
        """Method to create search parameters of `Gender Type of Pokémon`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, bool]]] | None:
            List with search parameters of `Gender Type of Pokémon`
            for elasticsearch
        """
        has_male, has_female = self.gender_type
        if has_male is None and has_female is None:
            return None

        gender_param_list: list[dict] = []

        match has_male:
            case "0":
                gender_param_list.append(
                    {"match": {"gender_type.has_male": False}}
                )
            case "1":
                gender_param_list.append(
                    {"match": {"gender_type.has_male": True}}
                )
            case _:
                pass

        match has_female:
            case "0":
                gender_param_list.append(
                    {"match": {"gender_type.has_female": False}}
                )
            case "1":
                gender_param_list.append(
                    {"match": {"gender_type.has_female": True}}
                )
            case _:
                pass

        if gender_param_list:
            return gender_param_list
        else:
            return None
