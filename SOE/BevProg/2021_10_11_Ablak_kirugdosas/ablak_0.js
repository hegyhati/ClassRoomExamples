
let nevek = ['Mate','Gina','Rebeka','Gina','Mate','Mate']
let count = [0,0,0,0,0,0]
let l = nevek.length
let counter = 0
let position = 0
console.log("1 eloszor")
console.log(nevek)
console.log(count)
console.log("\n")
for(let i = 0; i < l; i++){
    for(let j = 0; j < l; j++){
        if((nevek[i] === nevek[j]) && (i != j)){
            counter++
        }
    }
    count[i] = counter
    counter = 0
}
console.log("2 masodszor")
console.log(nevek)
console.log(count)
for(let i = 0; i < l; i++){
    if(count[position] < count[i]){
        position = i
    }
}
console.log("\n")
count[position]++
console.log("Leggyakrabban:", nevek[position], " rugta ki az ablakot, gyakorisaga:", count[position])
