function dontworry() {
    alert("Akkor ne aggódj miatta!")
}

const confirmmsg = "De most komolyan: igen vagy nem? (I/N)"
confirmmsg = "alma"

let problems = prompt("Vannak gondjaid? (I/N)")

while (problems !== "I" && problems !== "N" && problems !== "i" && problems !== "n") {
    problems = prompt(confirmmsg)
}

if (problems == "I" || problems == "i") {
    let doabout = prompt("Tudsz tenni valamit érte? (I/N)")
    while (doabout !== "I" && doabout !== "N" && doabout !== "i" && doabout !== "n") {
        doabout = prompt(confirmmsg)
    }
    if  (doabout == "I" || doabout == "i"){
        alert("Akkor oldd meg a problemadat!")
    } else {
        dontworry()
    }
}
else { dontworry() }
