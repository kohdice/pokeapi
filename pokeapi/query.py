from abc import ABC, abstractmethod
from typing import Any


class Param(ABC):
    @abstractmethod
    def create_param(self) -> dict[str, Any] | None:
        pass
