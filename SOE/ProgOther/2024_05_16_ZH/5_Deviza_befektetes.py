"""

## 5. Money-Money-Money - 6 pont

A feladat megoldasahoz az alabbi public API-t hasznald: 
https://github.com/hakanensari/frankfurter/blob/main/README.md

 - **a)** 2000-tol kezdve 2024-ig kerd le minden evre a januar 1 napi EUR/HUF arfolyamot, majd abrazold ezt egy diagrammon.
 - **b)** Szamold ki, hogyha minden evben januar 1-en 100000 Ft-ot eurora valtottunk volna 2000-tol 2023-ig, majd 2024 januar 1-en visszavaltottuk volna forintra, akkor a befektetett 2.4 millio Ft-bol mennyi penzunk lett volna. *BONUSZ*  Egy diagrammon abrazold, hogy mikent valtozott volna a penzunk erteke, ha atvaltjuk/nem vatljuk at a penzunket. 

"""

import requests
import matplotlib.pyplot as plt

url = "https://api.frankfurter.app/{}-01-01"

years = list(range(2000,2025))

EUR_to_HUF = []

for year in years:
    data = requests.get(url.format(year)).json()
    EUR_to_HUF.append(data["rates"]["HUF"])

print(EUR_to_HUF)

plt.plot(years, EUR_to_HUF)
plt.suptitle("EUR to HUF")
plt.savefig("5_EUR_to_HUF.png")


YEARLY_MONEY = 100_000
total_eur = 0
eur_value_in_huf = []
huf_value_in_huf = list(range(YEARLY_MONEY, 24*YEARLY_MONEY+1, YEARLY_MONEY)) + [24*YEARLY_MONEY]

for idx, year in enumerate(years[:-1]):
    total_eur += YEARLY_MONEY / EUR_to_HUF[idx]
    eur_value_in_huf.append(total_eur * EUR_to_HUF[idx])

final_huf = total_eur * EUR_to_HUF[-1]
eur_value_in_huf.append(final_huf)

print("Ha EURoban tartottam volna a penzem, 2.4 millio helyett ennyi lenne most:", final_huf)

plt.clf()
plt.plot(years, eur_value_in_huf, label = "EUR value in HUF")
plt.plot(years, huf_value_in_huf, label = "HUF value in HUF")
plt.legend()
plt.savefig("5_EUR_investment.png")



