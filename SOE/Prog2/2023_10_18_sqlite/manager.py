import sqlite3
from abc import ABC, abstractmethod, abstractclassmethod

@ABC
class Persistable:
    
    @abstractclassmethod
    def _sql_scheme(cls) -> str:
        pass
    
    def persist_command(self) -> str:
        return f"INSERT INTO {self._sql_table()} ({','.join(self._sql_fields())} VALUES ({','.join(['?']*len(self._sql_fields))})"
    
    @abstractclassmethod
    def _sql_fields(cls)->list[str]:
        pass

    @abstractmethod
    def _sql_values(self) -> list:
        pass



class DB_Manager:

    __tables = {
        "teams" : """
            name  TEXT PRIMARY KEY,
            city  TEXT NOT NULL,
            color TEXT NOT NULL,
            year  INTEGER
        """,
        "runners" : """
            nickname TEXT PRIMARY KEY,
            team     TEXT NOT NULL,
            FOREIGN KEY(team) REFERENCES team(name)
        """
    }
    
    def __init__(self, file:str = "running.db") -> None:
        self.__db = sqlite3.connect(file)
        self.__cursor = self.__db.cursor()
        if not self._db_structure_exists():
            self._initialize_db_structure()
    
    def __del__(self):
        self.__db.close()
    
    def _db_structure_exists(self) -> bool:
        return set(self.__tables.keys()).issubset(
            { row[0] for row in self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table'") }
        )

    def _initialize_db_structure(self) -> None:
        for tablename, structure in self.__tables.items():
            print(f"Creating table {tablename} with CREATE TABLE {tablename} ({structure})")
            self.__cursor.execute(f"CREATE TABLE {tablename} ({structure})")

    def persist(self, entity:Persistable) -> None:
        self.__cursor.execute(entity.persist_command(), entity._sql_values())


