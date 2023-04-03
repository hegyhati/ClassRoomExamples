

l = [1,2,3]

l2 = map(lambda x: -x, l)

print(list(l2))

l = [1,2,3,4,45]
print(sum(l))

people = [
    {
        "name": "Adam",
        "apple": 4
    },
    {
        "name": "Balazs",
        "apple": 23
    },
    {
        "name": "Erik",
        "apple": 0
    },
    {
        "name": "Gergo",
        "apple": 15
    },
    {
        "name": "Mate",
        "apple": 3
    }
]

from functools import reduce

total_apples = reduce(
    lambda cumulative_stuff,element: cumulative_stuff+element["apple"], 
    people, 0)

total_apples=0
for person in people:
    total_apples += person["apple"]

people_with_appletrees = []
for person in people:
    if person["apple"] >= 10:
        people_with_appletrees.append(person)

people_with_appletrees = filter(lambda p: p["apple"]>=10, people)

print(list(people_with_appletrees))