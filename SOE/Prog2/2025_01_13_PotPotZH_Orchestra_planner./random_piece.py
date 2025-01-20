import json
from random import choice, randrange

TYPE = ["Symphony", "Overture", "Concerto", "Suite", "Waltz", "March", "Fantasia", "Rhapsody", "Nocturne", "Serenade", "Capriccio", "Divertimento", "Ballade", "Intermezzo", "Variations", "Fugue", "Cantata", "Oratorio", "Scherzo"]
KEY = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"] 
SCALE = ["major", "minor"]

with open("PESZ.json") as f:
    instruments = {instrument: len(musicians) for instrument,musicians in json.load(f).items() }

def get_random_piece() -> dict:
    return {
        "name": f"{choice(TYPE)} in {choice(KEY)} {choice(SCALE)}",
        "instruments": { instrument : randrange(count) for instrument,count in instruments.items() }
    }

def get_random_pieces_with_distinct_names(count:int) -> list[dict]:
    pieces = {}
    while len(pieces) < count:
        piece = get_random_piece()
        pieces[piece["name"]] = piece
    return pieces.values()

print(get_random_pieces_with_distinct_names(5))