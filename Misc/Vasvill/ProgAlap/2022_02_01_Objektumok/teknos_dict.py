from math import sin, cos, pi


def eloremegy(teknosbeka, mennyit):
    teknosbeka["x"] += int(mennyit * cos(teknosbeka["szog"]*pi/180))
    teknosbeka["y"] += int(mennyit * sin(teknosbeka["szog"]*pi/180))


def jobbrafordul(teknosbeka, szog):
    teknosbeka["szog"] -= szog


def balrafordul(teknosbeka, szog):
    teknosbeka["szog"] += szog


teknosbeka = {
    "x": 0,
    "y": 0,
    "szog": 90
}

print(teknosbeka)
eloremegy(teknosbeka, 30)
jobbrafordul(teknosbeka, 90)
print(teknosbeka)
eloremegy(teknosbeka, 30)
jobbrafordul(teknosbeka, 90)
print(teknosbeka)
eloremegy(teknosbeka, 30)
jobbrafordul(teknosbeka, 90)
print(teknosbeka)
eloremegy(teknosbeka, 30)
jobbrafordul(teknosbeka, 90)
print(teknosbeka)
