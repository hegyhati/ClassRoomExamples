import enum

from typing import List, Optional
from sqlalchemy import ForeignKey, String, Enum, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Color(enum.Enum):
    other = 0
    blue = 1
    red = 2
    yellow = 3
    green = 4

    def __str__(self) -> str:
        match self:
            case Color.blue: return "K"
            case Color.red: return "P"
            case Color.yellow: return "S"
            case Color.green: return "Z"
            case Color.other: return ""


class Shape(enum.Enum):
    other = 0
    line = 1
    cross = 2
    triangle = 3
    circle = 4
    square = 5
    ruin = 6
    cave = 7

    def __str__(self) -> str:
        match self:
            case Shape.line: return "-"
            case Shape.cross: return "+"
            case Shape.triangle: return "hszg"
            case Shape.circle: return "kor"
            case Shape.square: return "negyzet"
            case Shape.ruin: return "L"
            case Shape.cave: return "omega"
            case Shape.other: return ""

class Base(DeclarativeBase):
    pass

class Route(Base):
    __tablename__ = "routes"
    id: Mapped[int] = mapped_column(primary_key=True)
    color : Mapped[Color]
    shape : Mapped[Shape]
    distance: Mapped[float]
    pois: Mapped[List["Visit"]] = relationship("Visit", back_populates="route") 

class POI(Base):
    __tablename__ = "POIs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =  mapped_column(String(30))
    description: Mapped[Optional[str]]
    routes: Mapped[List["Visit"]] = relationship("Visit", back_populates="poi")

class Visit(Base):
    __tablename__ = "visits"
    route_id : Mapped[int] = mapped_column(ForeignKey("routes.id"), primary_key=True)
    poi_id : Mapped[int] = mapped_column(ForeignKey("POIs.id"), primary_key=True)
    position : Mapped[float]
    route : Mapped[Route] = relationship("Route", back_populates="pois")
    poi : Mapped[POI] = relationship("POI", back_populates="routes")


if __name__ == "__main__":
    from sys import argv
    
    if len(argv) < 2: exit()
    engine = create_engine(f"sqlite:///{argv[1]}.sqlite", echo = True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import Session
    import json 

    session = Session(engine)
    with open("sopron.json") as f:
        data = json.load(f)
    
    poi_ids = {}
    for name, description in data["POIs"].items():
        poi = POI(name = name, description = description)
        session.add(poi)    
        session.flush()
        poi_ids[name] = poi.id
    
   
    for [color, shape, distance, pois] in data["routes"]:
        route = Route(
            color = {
                "K" : Color.blue,
                "P" : Color.red,
                "S" : Color.yellow,
                "Z" : Color.green
            }[color],
            shape = {
                "-" : Shape.line,
                "hszg" : Shape.triangle
            }[shape],
            distance = distance
        )
        session.add(route)
        session.flush()
        for name, position in pois.items():
            session.add(Visit(route_id = route.id, poi_id = poi_ids[name], position = position))

    session.commit()


