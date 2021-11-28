import json


if __name__ == "__main__":
    with open("ize.json") as file:
        data = json.load(file)
    for subject in data:
        print("Targynev:", subject["subject"], "Vizsganap:", subject["date"])
    new_subject = input("Mi a targy neve? ")
    new_hours = float(input("Hany orat kell ra tanulni? "))
    new_date = int(input("Melyik nap lesz a vizsga? "))
    new_subject = {
        "subject": new_subject,
        "date": new_date,
        "hours": new_hours
    }
    data.append(new_subject)
    print(data)
    with open("ize.json","wt") as file:
        json.dump(data,file)
