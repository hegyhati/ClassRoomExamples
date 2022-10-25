import json

# reads database from file by given filename
# TODO: crashes if file doesn't exist
def read_data(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

# returns the list of  trainings for a person
def get_trainings_for_person(database, name):
    trainings = []
    for training in database:
        if name in training["people"]:
            trainings.append(training)
    return trainings
    return [training for training in trainings if name in training["people"]]

# gets a time as a float (ex: 18.5) and returns it as a pretty string (ex:18:30)
def pretty_time(time):
    hour = int(time)
    minute = int(60 * (time%1))
    return f"{hour}:{minute:02}"


# Returns a pretty display name of the training
def pretty_training_name(training):
    days = ["Hetfo" , "Kedd", "Szerda", "Csutortok", "Pentek", "Szombat", "Vasarnap"]
    day = days[training['day']-1]
    start = pretty_time(training['start'])
    finish = pretty_time(training['start'] + training['duration'])
    return f"{training['sport']} ({day}, {start}-{finish})"

def print_trainings_for_person(database, person):
    trainings = get_trainings_for_person(database, person)
    if not trainings:
        print("Meg nem jelentkeztel tesire.")
    else:
        print("Ezekre vagy feljelentkezve:")
        for training in trainings:
            print(f" - {pretty_training_name(training)}")


database = read_data("soe_2022_osz.json")
name = input("Hogy hivnak? ")
print_trainings_for_person(database, name)