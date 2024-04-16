import json

with open("tea_data.json") as f:
    data = json.load(f)

def varname(farm,market): return f"{farm}_to_{market}"

with open("generated_tea_model.mod", "w") as f:
    # Variables
    for farm in data["farms"]:
        for market in data["markets"]:
            f.write(f"var {varname(farm,market)} >=0;\n")
    
    # Supply constraints
    for farm in data["farms"]:
        f.write(f"s.t. {farm}_supply:\n")
        for market in data["markets"]:
            f.write(f" + {varname(farm,market)} ")
        f.write(f" <= {data['farms'][farm]};\n")

    # Demand constraints
    for market in data["markets"]:
        f.write(f"s.t. {market}_demand:\n")
        for farm in data["farms"]:
            f.write(f" + {varname(farm,market)} ")
        f.write(f" >= {data['markets'][market]};\n")

    # Objective
    f.write("minimize Total_transportation_cost:\n")
    for farm in data["farms"]:
        for market in data["markets"]:
            f.write(f" + {data['distances'][farm][market]} * {varname(farm,market)} ")
    f.write(";\n")


# Pyomo