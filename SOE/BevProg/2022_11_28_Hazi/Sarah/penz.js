
function kiszamol() {
    let tizes = 10 * Number(document.getElementById("tizes").value)
    let huszas = 20 * Number(document.getElementById("huszas").value)
    let otvenes = 50 * Number(document.getElementById("otvenes").value)
    let szazas = 100 * Number(document.getElementById("szazas").value)
    let ketszazas = 200 * Number(document.getElementById("ketszazas").value)
    let osszesen = tizes + huszas + otvenes + szazas + ketszazas
    document.getElementById("vegosszeg").innerHTML = osszesen + "HUF"
}