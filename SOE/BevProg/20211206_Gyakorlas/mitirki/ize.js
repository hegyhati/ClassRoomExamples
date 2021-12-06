let m = [1,2,5,7,2,4,5]
for (let i = 0; i<4; i++) {
    console.log(i,m[i])
    m[i] -= i // m[i] = m[i] - i
}
console.log(m)

/*
------------------------------------
m : 
index: m[0] m[1] m[2] m[3] 4 5 6
ertek: 1    1    3    4    2 4 5

i: 4

Console: 
0 1
1 2
2 5
3 7 
[1, 1, 3, 4, 2, 4, 5]

*/
