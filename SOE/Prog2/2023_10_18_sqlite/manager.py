from model import Team, Runner
from persistable import Persistable
import sqlite3

class DB_Manager:

    __managed_types = (Team, Runner)
    
    def __init__(self, file:str = "running.db") -> None:
        self.__db = sqlite3.connect(file)
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("PRAGMA foreign_keys = ON;")
        self.__check_db_structure()

    def __del__(self):
        self.__db.close()

    def __check_db_structure(self) -> None:
        for type in self.__managed_types:
            if not self.__table_exist(type):
                self.__create_table(type)

    def __table_exist(self, type) -> bool:
        return len(self.__cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{type.__name__}'").fetchall()) == 1

    def __create_table(self, type) -> None:
            self.__cursor.execute(type.table_creation_command())

    def persist(self, entity:Persistable) -> None:
        try:
            self.__cursor.execute(entity.persist_command(), entity._sql_values())
            self.__db.commit()
        except sqlite3.IntegrityError as error:
            if "UNIQUE" in str(error):
                print(f"Entity {entity} already exists in database")
            elif "FOREIGN KEY" in str(error):
                print(f"Entity {entity} has an erroneous foreign key.")


