data = [
    {
        "name" : "Torok Daniel",
        "gender" : "male",
        "age" : 18
    },
    {
        "name" : "Patzer David",
        "gender" : "male",
        "age" : 21
    },
    {
        "name" : "Varga Attila",
        "gender" : "male",
        "age" : 62
    },
    {
        "name" : "Tirpak Dorina",
        "gender" : "female",
        "age" : 18
    }
]


# {18, 21, 62}
ages = { person["age"] for person in data }

# {"Dorina" : 18, "Attila": 62, "David": 21, "Daniel": 18}
foo = { person["name"].split(" ")[-1] : person["age"] for person in data}

print(ages, foo)
