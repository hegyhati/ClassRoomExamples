import matplotlib.pyplot as plt
import json

with open("data_20250415_195416.json") as (f):
    data = json.load(f)

fig,axs = plt.subplots(2)


axs[0].scatter(
    [ drone["position"]["latitude"] for drone in data["drones"]],
    [ drone["position"]["longitude"] for drone in data["drones"]],
    label = "Drones"
)
axs[0].scatter(
    [ drone["position"]["latitude"] for drone in data["chargingStations"]],
    [ drone["position"]["longitude"] for drone in data["chargingStations"]],
    label = "Charging stations"
)

axs[1].barh(
    [team["name"] for team in data["teams"]],
    [team["score"] for team in data["teams"]],
)
fig.legend()
fig.tight_layout()

fig.savefig("foo.png")