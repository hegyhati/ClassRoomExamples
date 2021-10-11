// Bemenet
let accidents_as_string = prompt("Kik rugtak ki az ablakokat? (vesszovel elvalasztva)")
let accidents = accidents_as_string.split(",")

// Bemenet debug tisztitas elot
console.log("Bemenet tisztitas elot",accidents_as_string, accidents)

// Bemene tisztitas
for (let i = 0; i < accidents.length; i++){
    accidents[i]=accidents[i].trim()
    accidents[i]=accidents[i].toLowerCase()
}

// Bemenet debug tisztitas utan
console.log("Bemenet tisztitas utan",accidents)

// Szamlalas inicializalas
let count = []
for (let i = 0; i < accidents.length; i++)
    count.push(0)

// Debug kiiratas
console.log("Osszeszamolas elott", accidents, count)

// Darabszam osszeszamolasa
for (let i = 0; i < accidents.length; i++) {
    for (let j = 0; j < accidents.length; j++) {
        if (accidents[i] === accidents[j]) {
            count[i]++
        }
    }
}

// Debug kiiratas
console.log("Osszeszamolas utan", accidents, count)

// Search for max index
let idx_of_max = 0
for (let i = 0; i < accidents.length; i++) {
    if (count[idx_of_max] < count[i]) {
        idx_of_max = i
    }
}

// print output
let prettyname=accidents[idx_of_max]
prettyname=prettyname.slice(0,1).toLocaleUpperCase() + prettyname.slice(1,prettyname.length)
alert(`Leggyakrabban: ${prettyname} rugta ki az ablakot, gyakorisaga: ${count[idx_of_max]}.`)
