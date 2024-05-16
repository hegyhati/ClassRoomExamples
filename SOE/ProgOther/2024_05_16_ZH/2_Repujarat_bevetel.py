"""

## 2. Repulo tulfoglalasok - 4 pont
Bevett gyakorlat, hogy a legitarsasagok tobb jegyet adnak el egy jaratra, mint ahany ulohely van, ismerve a statisztikakat, hogy nem mindenki jon tenylegesen el. Irj programot, mely beolvassa a jarat kapacitasat, a jegyek arait, az eladott jegyek szamat, megjelent utasok szamat, es a karterites merteket (ha valaki nem fer fel) es kiszamolja, hogy mennyi a bevetel. Pl.:
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 180
Kerem a megjelent utasok szamat: 180
Kerem a karterites merteket: 30000
A bevetel: 1800000
```
vagy
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 180
Kerem a megjelent utasok szamat: 20
Kerem a karterites merteket: 3000000000
A bevetel: 1800000
```
vagy
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 220
Kerem a megjelent utasok szamat: 150
Kerem a karterites merteket: 30000
A bevetel: 2200000
```
vagy
```
Kerem a jarat kapacitasat: 200
Kerem az egy jegy arat: 10000
Kerem az eladott jegyek szamat: 220
Kerem a megjelent utasok szamat: 210
Kerem a karterites merteket: 30000
A bevetel: 1900000
```

"""

capacity = int(input("Kerem a jarat kapacitasat: "))
ticket_price = int(input("Kerem az egy jegy arat: "))
sold_tickets = int(input("Kerem az eladott jegyek szamat: "))
travelers = int(input("Kerem a megjelent utasok szamat: "))
cancelation_fee = int(input("Kerem a karterites merteket: "))

revenue = sold_tickets * ticket_price
if travelers > capacity:
    canceled_trips = travelers - capacity
    revenue -= cancelation_fee * canceled_trips

print("A bevetel:", revenue)