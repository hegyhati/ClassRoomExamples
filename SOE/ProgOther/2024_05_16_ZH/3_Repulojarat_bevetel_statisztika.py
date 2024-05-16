"""

## 3. Repulojarat statisztika - 6 pont

Tegyuk fel, hogy:
 - 200 ferohelyes a jarat 
 - 10000 Ft egy jegy
 - 30000 Ft a karterites merteke
 - minden utas 95% esellyel jelenik meg
 - 210 jegyet adunk el

Irj programot, mely 1000 jaratot szimulal, kiszamolja, hogy hanyan jelennek meg, es mennyi lett a bevetel. Ezt abrazolja egy boxploton. 

**Bonusz** : Ismeteld meg a feladatot 200, 210, 220, 230 eladott jegyre, es azokat is abrazold egy boxploton.

"""

import random
import matplotlib.pyplot as plt

capacity = 200
sold_ticket_options = [200, 210, 220, 230]
ticket_price = 10_000
cancelation_fee = 30_000
chance_of_appearing = 0.95


revenue_results = []
for sold_tickets in sold_ticket_options:
    revenues = []
    for _ in range(1000):
        appeared = 0
        for person in range(sold_tickets):
            comes = random.uniform(0,1)
            if comes <= chance_of_appearing:
                appeared += 1

        revenue = sold_tickets * ticket_price
        if appeared > capacity:
            canceled_trips = appeared - capacity
            revenue -= cancelation_fee * canceled_trips
        revenues.append(revenue)
    revenue_results.append(revenues)

plt.boxplot(revenue_results, labels=sold_ticket_options)
plt.legend()
plt.savefig("3_airline_revenue.png")


