opciok = [
    "Plussmaci",
    "Konyv",
    "Csoki",
    "Virgacs",
    "Audi",
    "Disz",
    "Melleny",
    "Pulcsi",
    "Jatekauto"
]

puttony = []

function puttony_listaz() {
    let lista = document.getElementById("puttony_tartalom")
    for (ajandek in puttony) {
        lista.innerHTML += `<li>${ajandek}: ${puttony[ajandek]} db </li>`
    }
}

function puttonyba_tesz() {
    let ajandek = document.getElementById("ajandek").value
    if (ajandek in puttony) {
        puttony[ajandek] += 1
    } else {
        puttony[ajandek] = 1
    }
    
    novel()
    reset()
}

function novel(){
    let szamlalo = document.getElementById("szamlalo")
    szamlalo.innerHTML = Number(szamlalo.innerHTML) + 1
}

function reset() {
    document.getElementById("nev").value = ""
    document.getElementById("puttony_tartalom").innerHTML = ""
}

function inicializalas() {
    let select = document.getElementById("ajandek")
    for(ajandek of opciok){
        select.innerHTML += `<option value="${ajandek}">${ajandek}</option>`
    }
}
