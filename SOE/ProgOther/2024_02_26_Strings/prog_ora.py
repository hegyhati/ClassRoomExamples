hallgatok = []
nev = ""

while nev.lower() != "senki":
    nev = input("Ki a kovetkezo hallgato, aki bejott? ")
    hallgatok.append(nev.strip().title())

hallgatok.pop()

if len(hallgatok) >= 10:
    print("Nagyon boldog vagyok :-)")
elif len(hallgatok) >= 3:
    print("It's ok.")
else:
    print(":'(")

print("Ok jottek be:", end=" ")
for idx, hallgato in enumerate(hallgatok):
    if idx == len(hallgatok)-1:
        print(hallgato, end=".\n")
    else:
        print(hallgato, end=", ")

print("Ok jottek be: " + ", ".join(hallgatok) + ".")