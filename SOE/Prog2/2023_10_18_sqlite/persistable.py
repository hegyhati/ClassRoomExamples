from abc import ABC, abstractmethod
from typing import List


class Persistable(ABC):
    
    @classmethod
    @abstractmethod
    def _sql_scheme(cls) -> str:
        pass
    
    @classmethod
    def table_creation_command(cls) -> str:
        return f"CREATE TABLE {cls.__name__} ({cls._sql_scheme()})"
    
    @classmethod
    @abstractmethod
    def _sql_fields(cls)->List[str]:
        pass

    @abstractmethod
    def _sql_values(self) -> list:
        pass
    
    def persist_command(self) -> str:
        return f"INSERT INTO {type(self).__name__} ({','.join(self._sql_fields())}) VALUES ({','.join(['?']*len(self._sql_fields()))})"
    