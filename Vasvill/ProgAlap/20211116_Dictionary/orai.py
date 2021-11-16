verseny = {
    "nev" : "SPAR Budapest Maraton",
    "tav" : 42.2
}

verseny1 = {}
nev = input("Mi a verseny neve? ")
tav = float(input("Hany km hosszu a verseny? "))
verseny1["nev"] = nev
verseny1["tav"] = tav

verseny2 = {}
verseny2["nev"] = input("Mi a verseny neve? ")
verseny2["tav"] = float(input("Hany km hosszu a verseny? "))

verseny3 = {
    "nev" : input("Mi a harmadik verseny neve? "),
    "tav" : float(input("Mi a harmadik verseny tavja? "))
}

if verseny1["tav"] > verseny2["tav"]:
    print(verseny1["nev"],"a hosszabbik verseny")
else:
    print(verseny2["nev"],"a hosszabbik verseny")
