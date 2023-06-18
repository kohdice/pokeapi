from abc import ABC, abstractmethod

from . import param


class Query(ABC):
    """Abstract class for query creation"""

    @abstractmethod
    def create_query(self, target):
        """Abstract method for query creation"""
        pass


class CreatePokedexNumberQuery(Query):
    """Class with methods to create a query for elasticsearch
        that search for Pokémon by National Pokédex Number.

    Args:
        Param (object): Abstract class for query creation.
    """

    def create_query(
        self, pokedex_number: str | None
    ) -> dict[
        str, dict[str, dict[str, dict[str, dict[str, int]] | None]]
    ] | None:
        """Method to create a query for elasticsearch
            that searches for Pokémon by National Pokédex Number.

        Args:
            pokedex_number (str): National Pokédex Number of Pokémon.

        Returns:
            dict[
                str, dict[str, dict[str, dict[str, dict[str, str]] | None]]
            ] | None:
            Dict of query for elasticsearch to search for Pokémon
            by National Pokédex Number.

        """

        pokedex_number_param = param.CreatePokedexNumberParam(
            pokedex_number
        ).create_param()

        if pokedex_number_param is None:
            return None

        return {"query": {"bool": {"must": pokedex_number_param}}}


class CreatePokemonNameQuery(Query):
    """Class with methods to create a query for elasticsearch
        that search for Pokémon by name.

    Args:
        Param (object): Abstract class for query creation.
    """

    def create_query(
        self, pokemon_name: str | None
    ) -> dict[
        str, dict[str, dict[str, dict[str, dict[str, str]] | None]]
    ] | None:
        """Method to create a query for elasticsearch
            that searches for Pokémon by name.

        Args:
            pokemon_name (str): Name of Pokémon.

        Returns:
            dict[
                str, dict[str, dict[str, dict[str, dict[str, str]] | None]]
            ] | None:
            Dict of query for elasticsearch to search for Pokémon by name.
        """

        name_param = param.CreateNameParam(pokemon_name).create_param()

        if name_param is None:
            return None

        return {"query": {"bool": {"must": name_param}}}
