import json
import munka as MUNKA
import feladat as FELADAT

def kiir(beosztas):
    for munka in beosztas:
        MUNKA.kiir(munka) 

def beutemezheto(beosztas,ujmunka):
    for munka in beosztas:
        if MUNKA.utkozik(munka,ujmunka): return False
    return True

def uj_munka(beosztas):
    feladat=FELADAT.beker()
    munka=MUNKA.beutemez(feladat) 
    if beutemezheto(beosztas,munka): 
        beosztas.append(munka)
    else:
        print("Bocsi, utkozik valamivel.")

def betolt(fajlnev):
    try:
        infile=open(fajlnev,"rt")
        beosztas=json.load(infile)
        infile.close()
    except:
        beosztas=[]
    return beosztas

def kiment(beosztas,fajlnev):
    outfile=open(fajlnev,"wt")
    json.dump(beosztas,outfile)
    outfile.close()

def jelentes(beosztas):
    fajlnev=input("Melyik fajlba szeretnel jelentest generalni? ")
    fajl=open(fajlnev+".csv","wt")
    fejlecforma="{:10},{:10},{:10},,{:10},{:10}\n"
    sorforma="{0[nev]:10},{0[hatarido]:10},{0[idotartam]:10},,{1:10},{2:10}\n"
    fajl.write(fejlecforma.format("Feladat neve","Hatarido (nap)", "Idotartam(nap)","Elvallalt kezdes(nap)","Befejezes(nap)"))
    for munka in beosztas:
        (kezdes,befejezes)=MUNKA.intervallum(munka)
        fajl.write(sorforma.format(munka["feladat"],kezdes,befejezes))
    fajl.close()
