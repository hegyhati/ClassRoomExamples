import sys
import json

def varname(person, task):
    return person[0] + task[1:]

with open(sys.argv[1]) as f:
    data = json.load(f)

people = list(data.keys())
tasks = data[people[0]]

with open(sys.argv[1] + ".dat", "w") as f:
    f.write("set People := " + " ".join(people) + ";\n")
    f.write("set Tasks := " + " ".join(tasks) + ";\n")
    f.write("param time:\n")
    f.write(" ".join(tasks) + ":=\n")
    for person in people:
        f.write(person + " " + " ".join([str(data[person][task]) for task in tasks]))
        f.write("\n")
    f.write(";\n")