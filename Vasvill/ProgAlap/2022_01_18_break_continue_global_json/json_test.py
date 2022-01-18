import json

with open("homerseklet.json") as my_file:
     data = json.load(my_file)

for day in data:
    print("Homerseklet: ", day["temperature"])

t = float(input("Hany fok van? "))
h = int(input("Mennyi a paratartalom? "))

new_measurement = {
    "temperature" : t,
    "humidity": h
}

data.append(new_measurement)

print(data)

with open("homerseklet.json", "w") as my_file:
    json.dump(data,my_file, indent=1)