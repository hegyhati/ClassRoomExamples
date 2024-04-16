import json
import random

def generate_data(people, tasknumber, name):
    with open(f"{name}.json","w") as f:
        json.dump({
            person: {
                "T" + str(i) : random.randint(2,10)
                for i in range(tasknumber)
            } for person in people
        }, f)


generate_data(["Benedek", "Kakas", "Andras"], 100, "test3")