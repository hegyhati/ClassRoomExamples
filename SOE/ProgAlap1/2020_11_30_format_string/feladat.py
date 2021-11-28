def beker():
    nev = input("Mi a feladat neve? ")
    idotartam = int(input("Hany napig tart megcsinalni? "))
    hatarido = int(input("Meddig kell megcsinalni? "))
    return {"nev":nev, "idotartam":idotartam, "hatarido":hatarido}
