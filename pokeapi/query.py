from abc import ABC, abstractmethod


class Query(ABC):
    """Abstract class for query creation"""

    @abstractmethod
    def create_query(self, target):
        """Abstract method for query creation"""
        pass
