#!/usr/bin/python3

import json
from sys import argv


def varname(source,destination):
    return f"transport_from_{source}_to_{destination}"

with open(argv[1]) as f:
    data = json.load(f)

with open(argv[1] + ".mod","w") as f:    
    for factory in data["Supplies"]:
        for university in data["Demands"]:
            f.write(f"var {varname(factory,university)} >= 0;\n")
    f.write("\n\n")
    for factory in data["Supplies"]:
        f.write(f"s.t. {factory}_supply_constraint:\n\t")
        f.write(" + ".join([varname(factory,university) for university in data["Demands"]]))
        f.write(f" <= {data['Supplies'][factory]};\n\n")
    f.write("\n\n")
    for university in data["Demands"]:
        f.write(f"s.t. {university}_demand_constraint:\n\t")
        f.write(" + ".join([varname(factory,university) for factory in data["Supplies"]]))
        f.write(f" >= {data['Demands'][university]};\n\n")
    f.write("\n\n")
    f.write("minimize Trasportation_cost: "+ " + ".join([
        f"{data['Distances'][factory][university]} * {varname(factory,university)}"
        for factory in data["Supplies"]
        for university in data["Demands"]
    ]) + ";\n\n")
    f.write("end;\n")
    