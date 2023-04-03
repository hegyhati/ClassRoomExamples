l = [2,5,2,4,7,43,32,7,4,2,6]

print(l)
l.sort()
print(l)

people = [
    {
        "name": "Adam",
        "height": 174
    },
    {
        "name": "Balazs",
        "height": 196
    },
    {
        "name": "Erik",
        "height": 175
    },
    {
        "name": "Gergo",
        "height": 193
    },
    {
        "name": "Mate",
        "height": 186
    }
]

def get_height(person):
    return person["height"]

people.sort(key=get_height)

people.sort(key=lambda person: person["height"])

print(people)

