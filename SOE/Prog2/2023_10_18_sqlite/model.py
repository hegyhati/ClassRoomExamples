from dataclasses import dataclass
from typing import List
from persistable import Persistable

@dataclass
class Team (Persistable):
    name : str
    city : str
    color: str
    year : int

    @classmethod
    def _sql_scheme(cls) -> str : 
        return """
            name  TEXT PRIMARY KEY,
            city  TEXT NOT NULL,
            color TEXT NOT NULL,
            year  INTEGER
        """
    
    @classmethod
    def _sql_fields(cls)->List[str]:
        return ["name", "city", "color", "year"]
    
    def _sql_values(self) -> list:
        return [self.name, self.city, self.color, self.year]
        

@dataclass
class Runner (Persistable):
    nickname : str
    team : str

    @classmethod
    def _sql_scheme(cls) -> str : return """
            nickname TEXT PRIMARY KEY,
            team     TEXT NOT NULL,
            FOREIGN KEY(team) REFERENCES Team(name)
        """
    
    @classmethod
    def _sql_fields(cls)->List[str]:
        return ["nickname", "team"]
    
    def _sql_values(self) -> list:
        return [self.nickname, self.team]