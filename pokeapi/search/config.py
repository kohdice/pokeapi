import os
from dataclasses import dataclass
from typing import Any


class Singleton(type):
    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass(frozen=True)
class _ElasticsearchConfig(metaclass=Singleton):
    ES_INDEX: str | None
    ES_CONNECTION_URL: str | None


def get_config() -> _ElasticsearchConfig:
    return _ElasticsearchConfig(
        ES_INDEX=os.getenv("ES_INDEX"),
        ES_CONNECTION_URL=os.getenv("ES_CONNECTION_URL"),
    )
