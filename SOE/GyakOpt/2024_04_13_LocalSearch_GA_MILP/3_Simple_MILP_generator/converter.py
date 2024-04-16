import sys
import json

def varname(person, task):
    return person[0] + task[1:]

with open(sys.argv[1]) as f:
    data = json.load(f)

people = list(data.keys())
tasks = data[people[0]]

with open(sys.argv[1] + ".mod", "w") as f:
    for person in people:
        for task in tasks:
            f.write(f"var {varname(person, task)} binary;\n")
    f.write("var MS >= 0;\n")
    for task in tasks:
        f.write(f"s.t. {task}: {' + '.join([varname(person,task) for person in people])} = 1;\n")
    for person in people:
        f.write(f"s.t. {person}:\n\t")
        f.write(f"{' + '.join([ f'{data[person][task]} * {varname(person,task)}' for task in tasks])}")
        f.write(" <= MS;\n")
    f.write("minimize Makespan: MS;\n")


