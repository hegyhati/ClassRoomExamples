def szamjegyosszeg(szam):
    szoveg = str(szam)
    if len(szoveg) < 3:
        raise ValueError('Tul pici a szam')
    if len(szoveg) > 3:
        raise ValueError('Tul nagy a szam')
    return int(szam[0])+int(szam[1])+int(szam[2])


szam = input("Adj meg egy haromjegyu szamot:")
try:
    print(f"A {szam} szamjegyeinek osszege: {szamjegyosszeg(szam)}")
except ValueError as e:
    print("Nem jo bemenetet adtal meg: ", e)