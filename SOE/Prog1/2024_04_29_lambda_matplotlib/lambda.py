people = [
    {
        "name" : "Dzseni",
        "signatures" : 11
    },
    {
        "name" : "Dorina",
        "signatures" : 12
    },
    {
        "name" : "Atilla",
        "signatures" : 4
    }
]


### ProgAlap style

min_name = None
min_signature = 9999

for person in people:
    if person["signatures"] < min_signature:
        min_signature = person["signatures"]
        min_name = person["name"]

print(min_name)

### Trukkozos

names = [person["name"] for person in people]
signatures = [person["signatures"] for person in people]

min_idx = signatures.index(min(signatures))

print(names[min_idx])

### key

def get_signatures(person):
    return person["signatures"]

min_person = min(people, key=get_signatures)

print(min_person["name"])

### lambda

min_person = min(people, key = lambda person: person["signatures"])
print(min_person["name"])


