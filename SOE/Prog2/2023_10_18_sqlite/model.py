from dataclasses import dataclass
from manager import Persistable

@dataclass
class Team (Persistable):
    name : str
    city : str
    color: str
    year : int

    def __sql_scheme(cls) -> str : return """
            name  TEXT PRIMARY KEY,
            city  TEXT NOT NULL,
            color TEXT NOT NULL,
            year  INTEGER
        """
    
    def _sql_fields(cls)->list[str]:
        return ["name", "city", "color", "year"]
    
    def _sql_values(self) -> list:
        return [self.name, self.city, self.color, self.year]
        

@dataclass
class Runner (Persistable):
    nickname : str
    team : str

    def __sql_scheme(cls) -> str : return """
            nickname TEXT PRIMARY KEY,
            team     TEXT NOT NULL,
            FOREIGN KEY(team) REFERENCES team(name)
        """
    
    def _sql_fields(cls)->list[str]:
        return ["nickname", "team"]
    
    def _sql_values(self) -> list:
        return [self.nickname, self.team]