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
let count = {}
for (let i = 0; i < accidents.length; i++)
    count[accidents[i]]=0

// Debug kiiratas
console.log("Osszeszamolas elott", accidents, count)

// Darabszam osszeszamolasa
for (let name in count) {
    for (let j = 0; j < accidents.length; j++) {
        if (accidents[j] == name) {
            count[name]++
        }
    }
}

// Debug kiiratas
console.log("Osszeszamolas utan", accidents, count)

// Legnagyobb megkeresese
max = -1
for (let name in count) {
    if (max < count[name]) {
        max = count[name]
    }
}


// LEgrosszabbak kikeresese
let worst_people = []
for (let name in count) {
    if (count[name]==max) {
        let prettyname=name.slice(0,1).toLocaleUpperCase() + name.slice(1,name.length)
        worst_people.push(prettyname)
    }
}

// print output
alert(`Leggyakrabban: ${worst_people} rugta ki az ablakot, gyakorisaga: ${max}.`)
