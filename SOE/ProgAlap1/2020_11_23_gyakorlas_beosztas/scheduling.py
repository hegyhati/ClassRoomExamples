import json;

def feladat_beker():
    nev = input("Mi a feladat neve? ")
    idotartam = int(input("Hany napig tart megcsinalni? "))
    hatarido = int(input("Meddig kell megcsinalni? "))
    return {"nev":nev, "idotartam":idotartam, "hatarido":hatarido}

def feladat_beutemez(feladat):
    kezdes = int(input("Hanyadik naptol kezdjem el a feladatot? "))
    while kezdes + feladat["idotartam"] - 1 > feladat["hatarido"]:
        kezdes = int(input("Nem jo kezdes, hataridoig nem keszulne el, adj meg uj kezdest! "))
    return {"feladat":feladat, "kezdes":kezdes}

def munka_intervallum(munka):
    kezdes = munka["kezdes"]
    befejezes = kezdes + munka["feladat"]["idotartam"]-1
    return (kezdes,befejezes)

def munka_kiir(munka):
    nev = munka["feladat"]["nev"]
    (kezdes,befejezes) = munka_intervallum(munka)
    print(nev,": ",kezdes,"-",befejezes)

def beosztas_kiir(beosztas):
    for munka in beosztas:
        munka_kiir(munka)

def munka_utkozik(munka1,munka2):    
    (kezdes1,befejezes1) = munka_intervallum(munka1)
    (kezdes2,befejezes2) = munka_intervallum(munka2)
    return not (befejezes1 < kezdes2 or befejezes2 < kezdes1)

def beutemezheto(beosztas,ujmunka):
    for munka in beosztas:
        if munka_utkozik(munka,ujmunka): return False
    return True

def uj_munka(beosztas):
    feladat=feladat_beker()
    munka=feladat_beutemez(feladat)
    if beutemezheto(beosztas,munka): 
        beosztas.append(munka)
    else:
        print("Bocsi, utkozik valamivel.")

def beosztas_betolt(fajlnev):
    try:
        infile=open(fajlnev,"rt")
        beosztas=json.load(infile)
        infile.close()
    except:
        beosztas=[]
    return beosztas

def beosztas_kiment(beosztas,fajlnev):
    outfile=open(fajlnev,"wt")
    json.dump(beosztas,outfile)
    outfile.close()

def beosztas_jelentes(beosztas):
    fajlnev=input("Melyik fajlba szeretnel jelentest generalni? ")
    fajl=open(fajlnev+".csv","wt")
    fajl.write("Feladat neve,Hatarido (nap), Idotartam(nap),,Elvallalt kezdes(nap),Tervezett befejezes(nap)\n")
    for munka in beosztas:
        (kezdes,befejezes)=munka_intervallum(munka)
        fajl.write(munka["feladat"]["nev"])
        fajl.write(",")
        fajl.write(str(munka["feladat"]["hatarido"]))
        fajl.write(",")
        fajl.write(str(munka["feladat"]["idotartam"]))
        fajl.write(",")
        fajl.write(",")
        fajl.write(str(kezdes))
        fajl.write(",")
        fajl.write(str(befejezes))
        fajl.write("\n")
    fajl.close()

mentes_fajlnev=input("Melyik fajlbol szeretnel dolgozni? ")
beosztas=beosztas_betolt(mentes_fajlnev)
while True:
    valasz=input("Mit szeretnel csinalni? (uj/listaz/kilep/ment/jelentes) ")
    if valasz=="uj":
        uj_munka(beosztas)
    elif valasz == "listaz":
        beosztas_kiir(beosztas)
    elif valasz == "kilep":
        break
    elif valasz == "ment":
        beosztas_kiment(beosztas,mentes_fajlnev)
    elif valasz == "jelentes":
        beosztas_jelentes(beosztas)
    else:
        print("Ismeretlen parancs.")

