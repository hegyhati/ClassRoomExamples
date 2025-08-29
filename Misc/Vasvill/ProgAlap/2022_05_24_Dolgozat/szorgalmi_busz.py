
def osszead(ido1, ido2):
    ora1 = int(ido1.split(':')[0])
    perc1 = int(ido1.split(':')[1])
    ora2 = int(ido2.split(':')[0])
    perc2 = int(ido2.split(':')[1])
    ora = ora1 + ora2
    perc = perc1 + perc2
    if perc >= 60:
        ora += 1
        perc -= 60
    if perc < 10:
        perc = "0"+str(perc)
    return f"{ora}:{perc}"

def orat_percet_kinyer(ido):
    ora = int(ido.split(':')[0])
    perc = int(ido.split(':')[1])
    return ora, perc

def orat_percet_kinyer_2(ido):
    [ora, perc] = ido.split(':')
    return int(ora), int(perc)

def osszead_2(ido1, ido2):
    ora1, perc1 = orat_percet_kinyer(ido1)
    ora2, perc2 = orat_percet_kinyer(ido2)
    ora = (ora1 + ora2 + (perc1 + perc2)//60) % 24
    perc = (perc1 + perc2) % 60
    return f"{ora}:{perc:02}"

def helyi_menetrend(jarat_menetrend, jarat_indulasok, megallo):
    busz_erkezesek = []
    for indulas in jarat_indulasok:
        erkezes = osszead_2(indulas,jarat_menetrend[megallo])
        busz_erkezesek.append(erkezes)
    return busz_erkezesek


jarat_menetrend = {
    "Sopron" : "0:00",
    "Gorbehalom": "0:20",
    "Brennbergbanya": "0:35"
}

jarat_indulasok = ["8:00", "8:15", "8:40", "8:55", "10:23", "23:32"]

for megallo in jarat_menetrend:
    print(megallo,": ", helyi_menetrend(jarat_menetrend, jarat_indulasok, megallo))
