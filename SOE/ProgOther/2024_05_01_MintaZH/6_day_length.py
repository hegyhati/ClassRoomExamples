"""

## 6. Naphosszok

A feladat megoldasahoz az alabbi public API-t hasznald: https://sunrise-sunset.org/api
 - **a)** Kerd le, hogy Sopronban milyen hosszu egy nap minden honap elsejen (iden), es abrazold egy vonaldiagrammon. (2024-01-01-tol 2025-01-01-ig, tehat 13 pont legyen.)
 - **b)** Ismeteld meg ugyanezt Reykjavik-ra, Sydney-re, es azokat is tedd ra a diagrammra.


"""


import requests
import matplotlib.pyplot as plt

url = "https://api.sunrise-sunset.org/json?lat={}&lng={}&date={}&formatted=0"

dates = [ f"2023-{month+1}-01" for month in range(12)] + ["2024-01-01"]
cities = {
    "Sopron": {"lon" : 47.68166190, "lat" : 16.58447950 },
    "Reykjavik": {"lon" : 64.128288, "lat" : -21.827774 },
    "Sydney": {"lon" : -33.865143, "lat" : 151.209900 }
}

sopron_lengths = []
reykjavik_lengths = []
sydney_lengths = []

for date in dates:
    print("Getting data for", date)
    sopron_lengths.append(requests.get(url.format(cities["Sopron"]["lat"], cities["Sopron"]["lon"], date)).json()["results"]["day_length"])
    reykjavik_lengths.append(requests.get(url.format(cities["Reykjavik"]["lat"], cities["Reykjavik"]["lon"], date)).json()["results"]["day_length"])
    sydney_lengths.append(requests.get(url.format(cities["Sydney"]["lat"], cities["Sydney"]["lon"], date)).json()["results"]["day_length"])

plt.plot(dates, sopron_lengths, label="Sopron")
plt.plot(dates, reykjavik_lengths, label="Reykjavik")
plt.plot(dates, sydney_lengths, label="Sydney")
plt.xticks(rotation=45)
plt.legend()
#plt.show()
plt.savefig("Sopron_Reykjavik_Sydney_2024_day_length.png")