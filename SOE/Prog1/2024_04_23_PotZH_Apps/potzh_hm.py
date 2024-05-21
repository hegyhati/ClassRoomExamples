import json
from statistics import mean

def filename(year,month):
    return f"{year}-{month:02}.json"

def load_data (year,month):
    with open(filename(year,month)) as f:
        return json.load(f)
    
def day_usage(day):
    return sum([usage for usage in day["usage"].values()])

def monthly_usage(month):
    return sum(day_usage(day) for day in month)

WEEKDAYS = ["Hetfo", "Kedd", "Szerda", "Csutortok", "Pentek", "Szombat", "Vasarnap"]

def daily_averages(month):
    usages = [
        [day_usage(day) for day in month if day["weekday"] == daypos ]
        for daypos in range(7)
    ]
    for pos,name in enumerate(WEEKDAYS):
        print(f"{name}: {mean(usages[pos])} perc")

def get_apps(month):
    return {app for day in month for app in day["usage"].keys()}

def app_usage(month, app):
    return sum(day['usage'].get(app, 0) for day in month)

def app_summary(month):
    apps = get_apps(month)
    for app in apps:
        print(f"{app}: {app_usage(month,app)} perc")
    

def category_summary(month):
    with open("apps.json") as f:
        categories = json.load(f)
    for category, applist in categories.items():
        print(f"{category}: {sum(app_usage(month, app) for app in applist)} perc")
    
year = int(input("Ev:"))
month = int(input("Honap: "))
data = load_data(year,month)

print(f"{filename(year,month)} betoltve!")
print(f"Osszes hasznalati ido: {monthly_usage(data)} perc")
min_day = min(data, key=lambda day: day_usage(day))
print(f"Minimum: {min_day['date']} {day_usage(min_day)} perc")
max_day = max(data, key=lambda day: day_usage(day))
print(f"Maximum: {max_day['date']} {day_usage(max_day)} perc")

while True:
    choice = int(input("""
        Lehetőségek:
            1: Napi átlagok
            2: Összesítés appok szerint
            3: Összesítés kategóriák szerint
            0: Kilépés
        Válasszon menüpontot: """))
    match choice:
        case 0: break
        case 1: daily_averages(data)
        case 2: app_summary(data)
        case 3: category_summary(data)
