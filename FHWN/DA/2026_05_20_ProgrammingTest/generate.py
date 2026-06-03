import random

names = [
    "Bella", "Luna", "Charlie", "Lucy", "Cooper", "Max", "Daisy", "Milo", "Bailey", "Lola",
    "Sadie", "Rocky", "Buddy", "Molly", "Bear", "Duke", "Zoey", "Tucker", "Oliver", "Stella",
    "Teddy", "Roxy", "Bentley", "Maggie", "Leo", "Chloe", "Jack", "Lily", "Finn", "Penny",
    "Harley", "Nala", "Winston", "Gracie", "Louie", "Sophie", "Murphy", "Ruby", "Jax", "Rosie",
    "Gus", "Ellie", "Zeus", "Willow", "Moose", "Piper", "Toby", "Mia", "Bruno", "Coco",
    "Archie", "Ginger", "Odin", "Pepper", "Henry", "Hazel", "Dexter", "Abby", "Buster", "Millie",
    "Riley", "Annie", "Jake", "Emma", "Samson", "Layla", "Kobe", "Sasha", "Marley", "Izzy",
    "Scout", "Lexi", "Hank", "Athena", "Diesel", "Bonnie", "Thor", "Phoebe", "Ace", "Princess",
    "Blue", "Cookie", "Apollo", "Shadow", "Beau", "Kona", "Rex", "Dakota", "Simba", "Callie",
    "Otis", "Koda", "Bandit", "Olive", "Tank", "Nova", "Lucky", "Josie", "Rusty", "Maple",
]

adjectives = [
    "Fast", "Curious", "Sleepy", "Fluffy", "Grumpy", "Happy", "Lazy", "Energetic", "Brave", "Shy",
    "Clumsy", "Playful", "Gentle", "Fierce", "Dizzy", "Bouncy", "Sneaky", "Goofy", "Mighty", "Tiny",
    "Chubby", "Speedy", "Fuzzy", "Grumpy", "Jolly", "Noisy", "Quiet", "Silly", "Witty", "Scruffy",
    "Chunky", "Peppy", "Rowdy", "Spunky", "Fluffy", "Feisty", "Wobbly", "Snuggly", "Frisky", "Hyper",
    "Mellow", "Lively", "Jumpy", "Sturdy", "Cuddly", "Wacky", "Zippy", "Droopy", "Perky", "Grouchy",
]

breeds = [s.replace(" ","_") for s in [
    "Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog", "Bulldog",
    "Poodle", "Beagle", "Rottweiler", "Dachshund", "German Shorthaired Pointer",
    "Pembroke Welsh Corgi", "Siberian Husky", "Australian Shepherd", "Boxer", "Great Dane",
    "Doberman Pinscher", "Cavalier King Charles Spaniel", "Shih Tzu", "Boston Terrier", "Pomeranian",
    "Havanese", "Shetland Sheepdog", "Brittany", "English Springer Spaniel", "Cocker Spaniel",
    "Miniature Schnauzer", "Bernese Mountain Dog", "Cane Corso", "Pug", "Border Collie",
    "Basset Hound", "Maltese", "Chihuahua", "Vizsla", "Mastiff",
    "Weimaraner", "Newfoundland", "Collie", "West Highland White Terrier", "Bichon Frise",
    "Rhodesian Ridgeback", "Akita", "Saint Bernard", "Bloodhound", "Bull Terrier",
    "Airedale Terrier", "Whippet", "Alaskan Malamute", "Samoyed", "Australian Cattle Dog",
]]

dog_names = [ f"{a}_{n}" for a in adjectives for n in names ]

size = int(input("How many doggos? "))

dogs = random.sample(dog_names, k=size)

with open(f"dog_data.txt", "w") as f:
    f.write(f"Number of dogs: {size}\n")
    for dog in dogs:
        f.write(f"Name: {dog} Age: {random.randint(2,8)} Breed: {random.choice(breeds)}\n")

with open(f"incident_data.txt", "w") as f:
    incident_dates = sorted(random.choices([f"2025-{m:02d}-{d:02d}" for m in range(1,13) for d in range(1,29)], k=random.randint(size//2, size*int(size**0.8-1)//3)))
    for date in incident_dates:
        d1,d2 = random.sample(dogs, k=2)
        f.write(f"{date}: {d1} attacked {d2}\n")


