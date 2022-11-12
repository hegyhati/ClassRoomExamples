let eddigi_szavak = []

let elozo_szo = prompt("Kerem az elso szot:")
eddigi_szavak.push(elozo_szo)

let kovetkezo_szo = prompt("Kerem a masodik szot:")
while (elozo_szo==kovetkezo_szo){
    kovetkezo_szo = prompt("Ez volt az elso szo is, adj meg masikat.")
}

while (kovetkezo_szo[0] == elozo_szo[elozo_szo.length-1]) {
    eddigi_szavak.push(kovetkezo_szo)
    elozo_szo = kovetkezo_szo
    kovetkezo_szo = prompt("Kerem a kovetkezo szot:")
    while(eddigi_szavak.indexOf(kovetkezo_szo) != -1) {
        kovetkezo_szo = prompt("Ez mar volt, adjal meg masikat.")
    }
}

alert("Vesztettel.")
