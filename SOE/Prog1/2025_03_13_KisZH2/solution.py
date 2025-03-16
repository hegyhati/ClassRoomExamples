import json

with open("trains.json") as f:
    trains = json.load(f)

hour = int(input("Hour of departure? "))

stations = set()

for train in trains:
    if int(train["departure"][:2]) == hour:
    # if int(train["departure"].split(":")[0]) == hour:
        stations.update(train["stations"])
        # same as:
        # for station in train["stations"]:
        #     stations.add(station)

if not stations:
    print("No trains at this time.")
else:
    print("Destinations:")
    for station in stations:
        print(station)
