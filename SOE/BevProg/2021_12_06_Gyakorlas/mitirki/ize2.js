let m = 2
let k = 3
let l = [0,0,0,0,0,0]

while (m < 30) {
    l[m%5] += 1
    m += k
}
console.log(l)
