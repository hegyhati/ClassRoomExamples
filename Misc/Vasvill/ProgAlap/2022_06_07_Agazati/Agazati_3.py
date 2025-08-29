
import json


def get_Trails(poi):
    try:
        with open("soproni_jelzesek.json") as f:
            utvonalak = json.load(f)
    except FileNotFoundError:
        print("Nem található a soproni_jelzesek.json fájl.")
        exit()
    jelzesek = []
    for utvonal in utvonalak:
        if poi in utvonal["POI"]:
            jelzesek.append(utvonal["jelzes"])
    return jelzesek


for poi in ["Károly kilátó", "Hétbükkfa", "Valéta", "Erdő Háza", "Vasvilla"]:
    print(f"{poi}-t érintő jelzések: {', '.join(get_Trails(poi))}")