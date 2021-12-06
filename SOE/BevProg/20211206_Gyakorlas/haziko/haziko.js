function hozzaad(){
    let nev = document.getElementById("nev").value
    let szelesseg = Number(document.getElementById("szelesseg").value)
    let hosszusag = Number(document.getElementById("hosszusag").value)
    let terulet = szelesseg * hosszusag

    document.getElementById("lista").innerHTML += 
        `<li>${nev} - ${terulet} nm  (${szelesseg} X ${hosszusag})</li>`
    
    osszterulet_novel(terulet)
    reset()
    meretek()
}

function meretek() {
    let terulet = Number(document.getElementById("osszterulet").innerHTML)
    let meretek = document.getElementById("meretek")
    meretek.innerHTML = ""
    for(let sz=1;sz<=terulet;sz++){
        if(terulet % sz == 0) {
            console.log(sz,terulet/sz)
            meretek.innerHTML += `<tr><td>${sz}</td><td>${terulet/sz}</td></tr>`
        }
    }

}

function reset(){
    document.getElementById("nev").value = ""
    document.getElementById("szelesseg").value = 1
    document.getElementById("hosszusag").value = 1
}


function osszterulet_novel(uj_terulet){
    let terulet_span = document.getElementById("osszterulet")
    let eddigi_terulet = Number(terulet_span.innerHTML)
    eddigi_terulet += uj_terulet
    terulet_span.innerHTML=eddigi_terulet
}
