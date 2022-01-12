def udvozles(nev=None):
    if nev:
        return "Szia "+nev+"!"
    else:
        return "Szia!"


print(udvozles())
nev = input("Hogy hivnak? ")
print(udvozles(nev))
fantasy = input("Szereted a fantasy filmeket? ")
if fantasy == "igen":
    film = input("LotR vagy Twillight? ")
    if film == "LotR":
        kor = int(input("Hany eves vagy? "))
        if kor >= 18:
            print("Igyunk meg egy sort!")
        else:
            print("Vendegem vagy egy bambira.")
    else:
        print("Letagadom, hogy ismerlek.")
else:
    print("Bocsi, nincs mirol beszelgetnunk.")
