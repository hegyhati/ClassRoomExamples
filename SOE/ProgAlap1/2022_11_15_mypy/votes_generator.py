import random


file = "votes.txt"

seed = {
    "Shire" : [
        ("Frodo",  "Ringbearers"),
        ("Pippin" , "Pipe smokers"),
        ("Grima" , "Liars")
    ], 
    "Woods" : [
        ("Legolas" , "Elven Union"),
        ("Gandalf" , "Pipe Smokers"),
        ("Treebeard" , "Green party")
    ]
}

with open(file,"w") as f:
    for _ in range(random.randint(2000,3000)):
        district = random.choice(list(seed.keys()))
        vote = random.choice(seed[district])
        f.write(f"{district}, {vote[0]}, {vote[1]}\n")
