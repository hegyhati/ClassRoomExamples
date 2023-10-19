import json
import sys

def var(supply,demand): return f"transport_{supply}_{demand}"

with open(f"{sys.argv[1]}.json") as f:
    data = json.load(f)

with open(f"generated_{sys.argv[1]}.mod", "w") as f:
    # Variables
    for supply in data["supply"]:
        for demand in data["demand"]:
            f.write(f"var {var(supply,demand)} >= 0;\n")

    f.write("\n\n")
    # Supply constraints:
    for supply in data["supply"]:
        f.write(f"s.t. Max_supply_at_{supply}:\n")
        f.write(f"\t{' + '.join([var(supply,demand) for demand in data['demand']])} <= {data['supply'][supply]};\n")
    
    f.write("\n\n")
    # Demand constraints:
    for demand in data["demand"]:
        f.write(f"s.t. Min_demand_at_{demand}:\n")
        f.write(f"\t{' + '.join([var(supply,demand) for supply in data['supply']])} >= {data['demand'][demand]};\n")
    
    f.write("\n\n")
    #Objective:
    f.write("minimize Transportation_cost:\n\t")
    f.write(" + ".join([f'{data["distance"][supply][demand]} * {var(supply,demand)}' for demand in data["demand"] for supply in data["supply"]]))
    f.write(";\n")

