function szvb() {
    //alert ("Sikeres szavazat leadás!")
    document.getElementById("bogicount").innerHTML ++
    
}

function szva() {
    //alert ("Sikeres szavazat leadás!")
    document.getElementById("agicount").innerHTML ++
    
}

function szvr() {
    //alert ("Sikeres szavazat leadás!")
    document.getElementById("rekacount").innerHTML ++
    
}


 function kivezet() {
    let BC = Number(document.getElementById("bogicount").innerHTML)
    let AC = Number(document.getElementById("agicount").innerHTML)
    let RC = Number(document.getElementById("rekacount").innerHTML)
    if(BC >= AC && BC >= RC ) {
        winner = "Bogi";
    }
    else if (AC >= BC && AC >= RC) {
        winner = "Agi";
    }
    else {
        winner = "Reka";
    }
    alert (`A legtöbb szavazattal ${winner} rendelkezik!`)
 }
