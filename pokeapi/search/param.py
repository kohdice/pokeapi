from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Param(ABC):
    """Abstract class for parameter creation"""

    @abstractmethod
    def create_param(self) -> Any:
        """Abstract method for parameter creation"""
        pass


@dataclass
class CreatePokedexNumberParam(Param):
    """Dataclass to create search parameters for `National Pokédex Number`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    pokedex_number: int

    def create_param(self) -> list[dict[str, dict[str, int]]]:
        """Method to create search parameters of `National Pokédex Number`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, int]]]:
            List with search parameters of `National Pokémon Number`
            for elasticsearch
        """

        return [{"term": {"national_pokedex_number": self.pokedex_number}}]


@dataclass
class CreateNameParam(Param):
    """Dataclass to create search parameters for `Name of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    name: str

    def create_param(self) -> list[dict[str, dict[str, str]]]:
        """Method to create search parameters of `Name of Pokémon`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, str]]]:
            List with search parameters of `Name of Pokémon` for elasticsearch.
        """

        return [{"term": {"name": self.name}}]


@dataclass
class CreateFormParam(Param):
    """Dataclass to create search parameters of `Form of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    form: str | None

    def create_param(self) -> dict[str, dict[str, str]] | None:
        """Method to create search parameters of `Form of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, dict[str, str]] | None:
            Dict with search parameters of `Form of Pokémon` for elasticsearch.
        """

        if self.form is None:
            return None

        return {"term": {"form.keyword": self.form}}


@dataclass
class CreateRegionalVariantParam(Param):
    """Dataclass to create search parameters of `Regional Variant of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    regional_variant: str | None

    def create_param(self) -> dict[str, dict[str, str]] | None:
        """Method to create search parameters of `Regional Variant of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, dict[str, str]] | None:
            Dict with search parameters of `Regional Variant of Pokémon`
            for elasticsearch
        """

        if self.regional_variant is None:
            return None

        return {"term": {"regional_variant.keyword": self.regional_variant}}


@dataclass
class CreateMegaEvolutionParam(Param):
    """Dataclass to create search parameters of `Mega Evolution of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_mega_evolution: bool | None

    def create_param(self) -> dict[str, dict[str, bool]] | None:
        """Method to create search parameters of `Mega Evolution of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, dict[str, bool]] | None:
            Dict with search parameters of `Mega Evolution of Pokémon`
            for elasticsearch
        """

        match self.is_mega_evolution:
            case False:
                return {"term": {"is_mega_evolution": False}}
            case True:
                return {"term": {"is_mega_evolution": True}}
            case _:
                return None


@dataclass
class CreatePrimalReversionParam(Param):
    """Dataclass to create search parameters of `Primal Reversion of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_primal_reversion: bool | None

    def create_param(self) -> dict[str, dict[str, bool]] | None:
        """Method to create search parameters of `Primal Reversion of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, dict[str, bool]] | None:
            Dict with search parameters of `Primal Reversion of Pokémon`
            for elasticsearch
        """

        match self.is_primal_reversion:
            case False:
                return {"term": {"is_primal_reversion": False}}
            case True:
                return {"term": {"is_primal_reversion": True}}
            case _:
                return None


@dataclass
class CreateLegendaryParam(Param):
    """Dataclass to create search parameters of `Legendary of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_legendary: bool | None

    def create_param(self) -> dict[str, dict[str, bool]] | None:
        """Method to create search parameters of `Legendary of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, dict[str, bool]] | None:
            Dict with search parameters of `Legendary of Pokémon`
            for elasticsearch
        """

        match self.is_legendary:
            case False:
                return {"term": {"is_legendary": False}}
            case True:
                return {"term": {"is_legendary": True}}
            case _:
                return None


@dataclass
class CreateMythicalParam(Param):
    """Dataclass to create search parameters of `Mythical of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    is_mythical: bool | None

    def create_param(self) -> dict[str, dict[str, bool]] | None:
        """Method to create search parameters of `Mythical of Pokémon`
            for elasticsearch.

        Returns:
            dict[str, dict[str, bool]] | None:
            Dict with search parameters of `Mythical of Pokémon`
            for elasticsearch
        """

        match self.is_mythical:
            case False:
                return {"term": {"is_mythical": False}}
            case True:
                return {"term": {"is_mythical": True}}
            case _:
                return None


@dataclass
class CreateGenderTypeParam(Param):
    """Dataclass to create search parameters of `Gender Type of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    gender_type: tuple[bool | None, bool | None]

    def create_param(self) -> list[dict[str, dict[str, bool]]] | None:
        """Method to create search parameters of `Gender Type of Pokémon`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, bool]]] | None:
            List with search parameters of `Gender Type of Pokémon`
            for elasticsearch
        """

        if self.gender_type == (None, None):
            return None

        gender_param_list: list[dict] = []

        for k, v in zip(("has_male", "has_female"), self.gender_type):
            match v:
                case False:
                    gender_param_list.append(
                        {"term": {f"gender_type.{k}": False}}
                    )
                case True:
                    gender_param_list.append(
                        {"term": {f"gender_type.{k}": True}}
                    )
                case _:
                    continue

        if gender_param_list:
            return gender_param_list
        else:
            return None


@dataclass
class CreatePokemonTypeParam(Param):
    """Dataclass to create search parameters of `Type of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    pokemon_type: tuple[str | None, str | None]

    def create_param(
        self,
    ) -> list[dict[str, dict[str, str | list[str]]]] | None:
        """Method to create search parameters of `Type of Pokémon`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, str | list[str]]]] | None:
            List with search parameters of `Type of Pokémon`
            for elasticsearch
        """

        if self.pokemon_type == (None, None):
            return None

        pokemon_type_param_list: list[dict] = []

        for type_ in self.pokemon_type:
            if type_ is not None:
                pokemon_type_param_list.append(
                    {
                        "multi_match": {
                            "query": type_,
                            "fields": [
                                "pokemon_type.type_1.keyword",
                                "pokemon_type.type_2.keyword",
                            ],
                        }
                    }
                )

        return pokemon_type_param_list


@dataclass
class CreateAbilityParam(Param):
    """Dataclass to create search parameters of `Ability of Pokémon`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    abilities: tuple[str | None, str | None, str | None]

    def create_param(
        self,
    ) -> list[dict[str, dict[str, str | list[str]]]] | None:
        """Method to create search parameters of `Ability of Pokémon`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, str | list[str]]]] | None:
            List with search parameters of `Ability of Pokémon`
            for elasticsearch
        """

        if self.abilities == (None, None, None):
            return None

        ability_param_list: list[dict] = []

        for ability in self.abilities:
            if ability is not None:
                ability_param_list.append(
                    {
                        "multi_match": {
                            "query": ability,
                            "fields": [
                                "abilities.ability_1.keyword",
                                "abilities.ability_2.keyword",
                                "abilities.hidden_ability.keyword",
                            ],
                        }
                    }
                )

        return ability_param_list


@dataclass
class CreateKeywordParam(Param):
    """Dataclass to create search parameters of `keyword`
        for elasticsearch.

    Args:
        Param (object): Abstract class for search parameter creation.
    """

    keyword: str

    def create_param(
        self,
    ) -> list[dict[str, dict[str, str | list[str]]]]:
        """Method to create search parameters of `keyword`
            for elasticsearch.

        Returns:
            list[dict[str, dict[str, str | list[str]]]]:
            List with search parameters of `keyword`
            for elasticsearch
        """

        return [
            {
                "multi_match": {
                    "query": self.keyword,
                    "operator": "and",
                    "fields": [
                        "abilities.ability_1",
                        "abilities.ability_2",
                        "abilities.hidden_ability",
                        "form",
                        "name",
                        "pokemon_type.type_1",
                        "pokemon_type.type_2",
                        "regional_variant",
                    ],
                }
            }
        ]
