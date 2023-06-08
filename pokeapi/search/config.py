import os
from typing import Any


class Singleton(type):
    _instances: dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseConfig(metaclass=Singleton):
    def __init__(self) -> None:
        self.ES_INDEX = "pokemon"


class DevelopmentConfig(BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.ES_CONNECTION = "http://elasticsearch:9200"


class StagingConfig(BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.ES_CONNECTION = os.getenv("ES_CONNECTION_STAGING")


class ProductionConfig(BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.ES_CONNECTION = os.getenv("ES_CONNECTION_PRODUCTION")


class StageEnvIsWorngException(Exception):
    pass


def get_config() -> DevelopmentConfig | StagingConfig | ProductionConfig:
    match os.getenv("STAGE"):
        case "development":
            return DevelopmentConfig()
        case "staging":
            return StagingConfig()
        case "production":
            return ProductionConfig()
        case _:
            raise StageEnvIsWorngException(
                f"STAGE={os.getenv('STAGE')} is an invalid value."
            )
