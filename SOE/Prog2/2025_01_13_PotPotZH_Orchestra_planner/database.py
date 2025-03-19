import json
from typing import List
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Instrument(Base):
    __tablename__ = "instruments"
    name: Mapped[str] = mapped_column(primary_key=True)

class Musician(Base):
    __tablename__ = "musicians"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    instrument_name: Mapped[str] = mapped_column(ForeignKey("instruments.name"))
    instrument: Mapped[Instrument] = relationship(Instrument)


class Piece(Base):
    __tablename__ = "pieces"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    requirements: Mapped[List["Requirement"]] = relationship("Requirement")

class Requirement(Base):
    __tablename__ = "requirements"
    instrument_name: Mapped[str] = mapped_column(ForeignKey("instruments.name"), primary_key=True)
    piece_id: Mapped[int] = mapped_column(ForeignKey("pieces.id"), primary_key=True)
    count: Mapped[int]
    piece: Mapped[Piece] = relationship(Piece)


if __name__ == "__main__":
    engine = create_engine(f"sqlite:///PESZ.sqlite", echo = True)
    Base.metadata.create_all(engine)

    from sys import argv
    from sqlalchemy.orm import Session
    from random_piece import get_random_pieces_with_distinct_names
    import json 

    if len(argv) >= 2:         
        with Session(engine) as session:
            with open("PESZ.json") as f:
                PESZ = json.load(f)

            for instrument_name,musicians in PESZ.items():
                instrument = Instrument(name=instrument_name)
                session.add(instrument)
                session.flush()
                for musician_name in musicians:
                    session.add(Musician(name=musician_name, instrument=instrument))
                session.flush()
            session.commit()

            for piece_dict in get_random_pieces_with_distinct_names(int(argv[1])):
                piece = Piece(name=piece_dict["name"])
                session.add(piece)
                session.flush()
                for instrument_name, count in piece_dict["instruments"].items():
                    if count != 0:
                        session.add(Requirement(piece=piece, instrument_name=instrument_name, count=count))
                session.flush()
            session.commit()





