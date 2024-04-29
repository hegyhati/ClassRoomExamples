people = [
    {
        "name" : "Akos",
        "height" : 181,
        "weight": 106
    },
    {
        "name" : "Adrian",
        "height" : 155,
        "weight": 196
    },
    {
        "name" : "Lori",
        "height" : 186,
        "weight": 94
    },
    {
        "name" : "Dani",
        "height" : 178,
        "weight": 65
    }
]

most_heavy_person = max(people, key=lambda person: person["weight"])
print(most_heavy_person)

shortest_person = min(people,key=lambda person: person["height"])
print(shortest_person)


most_fit = min(people, key= lambda person: person["weight"] / (person["height"]/100) ** 2)
# vagy
def bmi(person):
    return person["weight"] / person["height"] ** 2
most_fit = min(people, key= bmi)

print(most_fit)