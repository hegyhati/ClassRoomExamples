import json
import random

supply_count = int(input("Supply count: "))
demand_count = int(input("Demand count: "))

demands = {
    f"Demand_{d}" : random.randint(50,500)
    for d in range(demand_count)
}

total_demand = sum(demands.values())

supplies = {
    f"Supply_{s}" : total_demand / supply_count
    for s in range(supply_count)
}

for _ in range(random.randrange(supply_count, supply_count*4)):
    s1 = random.randrange(supply_count)
    s2 = random.randrange(supply_count)
    move = random.randint(min(supplies[f"Supply_{s1}"],supplies[f"Supply_{s2}"])//5,min(supplies[f"Supply_{s1}"],supplies[f"Supply_{s2}"])//2)
    supplies[f"Supply_{s1}"] -= move
    supplies[f"Supply_{s2}"] += move

x = {
    f"Demand_{d}" : random.randint(0,1000)
    for d in range(demand_count)
}
x.update({
    f"Supply_{s}" : random.randint(0,1000)
    for s in range(supply_count)
})
y = {
    f"Demand_{d}" : random.randint(0,1000)
    for d in range(demand_count)
}
y.update({
    f"Supply_{s}" : random.randint(0,1000)
    for s in range(supply_count)
})

distances = {
    supply : {
        demand : ( (x[demand]-x[supply])**2 + (y[demand]-y[supply])**2)**0.5
        for demand in demands.keys()
    } 
    for supply in supplies.keys()
}

with open(f"data_{demand_count}_{supply_count}.json","w") as f:
    json.dump({
        "supply" : supplies,
        "demand" : demands,
        "distance" : distances
    }, f)