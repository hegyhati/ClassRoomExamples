
import json


with open("covid.json") as file:
    covid_data = json.load(file)


for day in covid_data:
    print(day["date"],":",day["new"])


d = input("Date: (YYYY-MM-DD) ")
n = int(input("New cases? "))
r = int(input("Recovered people? "))

new_day = {
    "date" : d,
    "new" : n,
    "recovered" : r
}

covid_data.append(new_day)

print(covid_data)

with open("covid.json", "w") as file:
   json.dump(covid_data, file, indent=2)