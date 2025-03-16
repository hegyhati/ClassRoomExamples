import json
from random import randrange, choice, sample, randint

stations = [
    "Budapest-Deli",
    "Budapest-Kelenfold",
    "Biatorbagy",
    "Bicske",
    "Tatabanya",
    "Tata",
    "Almasfuzito",
    "Komarom",
    "Acs",
    "Gyor",
    "Csorna",
    "Kapuvar",
    "Fertoszentmiklos",
    "Sopron",
]

with open("trains.json", "w", encoding="utf-8") as f:
    data = []
    for id in range(42):
        train = {
            "train_id": id,
            "seat_resevation": choice([True, False]),
            "departure": f"{randrange(4, 24):02}:{randrange(60):02}",
            "stations": sorted(sample(stations, k=randint(3, 6)), key=stations.index),
        }
        if randrange(2) == 1:
            train["stations"].reverse()
        data.append(train)
    json.dump(data, f, indent=2, ensure_ascii=False)
