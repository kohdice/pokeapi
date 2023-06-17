from abc import abstractmethod


class Query:
    """Abstract class for query creation"""

    @abstractmethod
    def create_query(self):
        """Abstract method for query creation"""
        pass
