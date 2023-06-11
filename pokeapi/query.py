from abc import ABC, abstractmethod
from typing import Any


class Param(ABC):
    @abstractmethod
    def create_param(self, target: str) -> dict[str, Any] | None:
        pass
