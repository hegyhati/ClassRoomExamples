import json


with open("measurements.json") as f:
    data = json.load(f)

good_data = [ float(item) for item in data if item != None ]
print(good_data)

