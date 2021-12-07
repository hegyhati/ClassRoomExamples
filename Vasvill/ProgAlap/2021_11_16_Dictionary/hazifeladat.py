mikortol = input("Mikor kezdodott az ora? ").split(":")
meddig = input("Meddig tartott az ora? ").split(":")

mikortol_percekben = int(mikortol[0])*60 + int(mikortol[1])
meddig_percekben = int(meddig[0])*60 + int(meddig[1])

hossz = meddig_percekben - mikortol_percekben

if hossz < 60:
    print("Osszesen",hossz,"percig tartott az ora.")
else:
    print("Oszesen",hossz//60,"ora es ",hossz%60,"percig tartott az ora.")
