import json

def varname(s,d):
    return f"from_{s['name']}_to_{d['name']}"

with open("data.json") as f:
    data = json.load(f)

with open("generated.mod", "w") as f:
    # Variable declarations
    for s in data["sources"]:
        for d in data["destinations"]:
            f.write(f"var {varname(s,d)} >= 0;\n")
        
    f.write("\n")
    
    # Source capacity constraints
    for s in data["sources"]:
        f.write(f"s.t. {s['name']}_capacity_constraint:\n\t")
        for d in data["destinations"]:
            f.write(f" + {varname(s,d)}")
        f.write(f" <= {s['capacity']} ;\n")
    
    f.write("\n")
    
    # Destination demand constraints
    for d in data["destinations"]:
        f.write(f"s.t. {d['name']}_demand_constraint:\n\t{' + '.join([varname(s,d) for s in data['sources']])} >= {d['demand']} ;\n")
    
    f.write("\n")
    
    # Objective
    f.write("minimize Cost:\n")
    for s in data["sources"]:
        for d in data["destinations"]:
            f.write(f" + {data['distances'][s['name']+'-'+d['name']]} * {varname(s,d)}")
    f.write(";\n")
    

