import json

def vname(student,subject):
    return student+"_megcsinal_"+subject

data = json.load(open("allamvizsga_data.json"))
students=data["students"]
subjects=data["subjects"]
prices=data["price"]

output = open("allamvizsga_total_generated.mod","wt")
for student in students:
    for subject in subjects:
        output.write(f"var {vname(student,subject)} binary;\n")

output.write("\n\n")

for student in students:
    output.write(f"s.t. {student}:\n")
    output.write(f"\t{data['max']} >= 0")
    for subject in subjects:
        output.write(f" + {vname(student,subject)} ")
    output.write(f" >= {data['min']};\n\n")
    
for subject in subjects:
    output.write(f"s.t. {subject}:\n")
    output.write("\t0")
    for student in students:
        output.write(f" + {vname(student,subject)} ")
    output.write(" = 1;\n\n")

output.write("minimize Osszesora:\n")
output.write("\t0")
for student in students:
    for subject in subjects:
        output.write(f" + {prices[student][subject]} * {vname(student,subject)} ")
output.write(";\n\n")

output.write("end;\n\n")
