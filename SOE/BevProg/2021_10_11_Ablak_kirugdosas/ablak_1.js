// Bemenet
let accidents = ['Mate','Gina','Rebeka','Gina','Mate','Mate','Gina','Gina','Mate','Mate','Gina','Gina','Mate','Mate','Gina','Gina','Mate','Mate','Gina']

// Szamlalas inicializalas
let count = []
for (let i=0; i<accidents.length; i++)
    count.push(0)

// Debug kiiratas
console.log("Osszeszamolas elott",accidents,count)

// Darabszam osszeszamolasa
for(let i = 0; i < accidents.length; i++){
    for(let j = 0; j < accidents.length; j++){
        if(accidents[i] === accidents[j]){
            count[i]++
        }
    }
}

// Debug kiiratas
console.log("Osszeszamolas utan",accidents,count)

// Search for max index
let idx_of_max = 0
for(let i = 0; i < accidents.length; i++){
    if(count[idx_of_max] < count[i]){
        idx_of_max = i
    }
}

// print output
alert(`Leggyakrabban: ${accidents[idx_of_max]} rugta ki az ablakot, gyakorisaga: ${count[idx_of_max]}.`)
