import beosztas as BEOSZTAS

mentes_fajlnev=input("Melyik fajlbol szeretnel dolgozni? ")
beosztas=BEOSZTAS.betolt(mentes_fajlnev)
while True:
    valasz=input("Mit szeretnel csinalni? (uj/listaz/kilep/ment/jelentes) ")
    if valasz=="uj":
        BEOSZTAS.uj_munka(beosztas)
    elif valasz == "listaz":
        BEOSZTAS.kiir(beosztas)
    elif valasz == "kilep":
        break
    elif valasz == "ment":
        BEOSZTAS.kiment(beosztas,mentes_fajlnev)
    elif valasz == "jelentes":
        BEOSZTAS.jelentes(beosztas)
    else:
        print("Ismeretlen parancs.")

