import json

station = input()

with open("data.json") as f:
    trains = json.load(f)

for train in trains:
    if not train["seat_resevation"] and station in train["stations"]:
        print(train["train_id"])
