"""

## BONUSZ: 6. Petofi szinhaz munkatarsai - 6 pont

Irj programot, mely a Petofi szinhaz oldalarol (https://www.soproniszinhaz.hu/) kigyujti, es 1-2 listaban kiirja a szinmuveszeket, tancmuveszeket es eloadomuveszeket.

"""


import requests
from bs4 import BeautifulSoup

url = "https://www.soproniszinhaz.hu/tarsulat.html"
site = requests.get(url)
soup = BeautifulSoup(site.content, "html.parser")

employee_divs = soup.find_all("div", class_="teamItem")

actors = []
dancers = []
musucians = []

for div in employee_divs:
    name = div.find("img").get("alt")
    role = div.find(class_="title").find("span").text
    if "színművész" in role:
        actors.append(name)
    if "táncművész" in role:
        dancers.append(name)
    if "előadóművész" in role:
        musucians.append(name)


print("Színészek:")
for actor in actors:
    print(f" - {actor}")
print("\nTáncosok:")
for dancer in dancers:
    print(f" - {dancer}")
print("\nZenészek:")
for musician in musucians:
    print(f" - {musician}")

