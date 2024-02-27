hallgatok = input("Kik jottek be? (vesszovel elvalasztva) ")
hallgato_lista = hallgatok.split(",")

if len(hallgato_lista) >= 10:
    print("Nagyon boldog vagyok :-)")
elif len(hallgato_lista) >= 3:
    print("It's ok.")
else:
    print(":'(")

print(hallgato_lista)

for hallgato in hallgato_lista:
    print(" - "+ hallgato.strip() )

