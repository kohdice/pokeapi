from abc import ABC, abstractmethod
from typing import Any

from . import param


class Query(ABC):
    """Abstract class for query creation"""

    @abstractmethod
    def create_query(self, target: Any) -> Any:
        """Abstract method for query creation"""
        pass


class CreatePokedexNumberQuery(Query):
    """Class with methods to create a query for elasticsearch
        that search for Pokémon by National Pokédex Number.

    Args:
        Param (object): Abstract class for query creation.
    """

    def create_query(
        self, pokedex_number: int
    ) -> dict[str, dict[str, dict[str, list[dict[str, dict[str, int]]]]]]:
        """Method to create a query for elasticsearch
            that searches for Pokémon by National Pokédex Number.

        Args:
            pokedex_number (str): National Pokédex Number of Pokémon.

        Returns:
            dict[str, dict[str, dict[str, list[dict[str, dict[str, int]]]]]]:
            Dict of query for elasticsearch to search for Pokémon
            by National Pokédex Number.

        """

        pokedex_number_param = param.CreatePokedexNumberParam(
            pokedex_number
        ).create_param()

        return {"query": {"bool": {"must": pokedex_number_param}}}


class CreatePokemonNameQuery(Query):
    """Class with methods to create a query for elasticsearch
        that search for Pokémon by name.

    Args:
        Param (object): Abstract class for query creation.
    """

    def create_query(
        self, pokemon_name: str
    ) -> dict[str, dict[str, dict[str, list[dict[str, dict[str, str]]]]]]:
        """Method to create a query for elasticsearch
            that searches for Pokémon by name.

        Args:
            pokemon_name (str): Name of Pokémon.

        Returns:
            dict[str, dict[str, dict[str, list[dict[str, dict[str, str]]]]]]:
            Dict of query for elasticsearch to search for Pokémon by name.
        """

        name_param = param.CreateNameParam(pokemon_name).create_param()

        return {"query": {"bool": {"must": name_param}}}


class CreateConditionalSearchQuery(Query):
    """Class with methods to create a query for elasticsearch
        that search for Pokémon by some conditions.

    Args:
        Param (object): Abstract class for query creation.
    """

    def create_query(
        self, conditions: tuple[Any, ...]
    ) -> dict[str, dict[str, dict[str, list[Any]]]]:
        """Method to create a query for elasticsearch
            that searches for Pokémon by some conditions.

        Args:
            conditions (tuple): Conditions of search.

        Returns:
            dict[str, dict[str, dict[str, list[Any]]]] | None:
            Dict of query for elasticsearch to search for Pokémon
            by some conditions.
        """

        condition_params: list[dict] = []

        for condition in conditions:
            param = condition.create_param()

            if param is None:
                continue

            if isinstance(param, list):
                condition_params.extend(param)
            else:
                condition_params.append(param)

        else:
            return {"query": {"bool": {"must": condition_params}}}
