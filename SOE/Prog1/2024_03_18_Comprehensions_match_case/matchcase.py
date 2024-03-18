people = [
    {"name" : "Sanyi"},
    {"firstname" : "Jozsef", "lastname" : "Smidla"},
    {"nickname" : "Potyi"},
    {},
    None
]

for person in people:
    match person:
        case {"name": name} | {"nickname": name}:
            print(f"Hello {name}")
        case {"firstname":fname, "lastname":lname}:
            print(f"Hello {fname} {lname}.")
        case dict():
            print(f"Hello Anonymus")
        case other:
            print("Wrong data")