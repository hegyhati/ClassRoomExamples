import json

def print_practices_for_subject(subject: str):
    with open("summer_practice.json") as f:
        data = json.load(f)
    for student in data:
        if subject in data[student]:
            hours = data[student][subject]
            if hours > 0 :
                print(f"{student} practiced {hours} hours.")
            elif hours == 0:
                print(f"{student} didn't practice")
            else:
                print(f"{student} forgot what he/she knew.")
        else:
            print(f"{student} didn't practice")

def register_new_practice():
    student = input("Name: ")
    subject = input("Subject: ")
    hours = int(input("Hours: "))
    with open("summer_practice.json") as f:
        data = json.load(f)
    if student in data:
        if subject in data[student]:
            data[student][subject] += hours
        else:
            data[student][subject] = hours
    else:
        data[student] = {subject:hours}
    with open("summer_practice.json", "w") as f:
        json.dump(data,f)

if __name__ == "__main__":
    register_new_practice()