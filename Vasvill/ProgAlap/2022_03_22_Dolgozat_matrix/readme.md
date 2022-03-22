# Órai feladatok
1. Írj programot, mely bekér egy számot (`n`), és elkészít egy `n`x`n`-es mátrixot (listába ágyazott lista), benne csupa `0`-val.
2. Szervezd ki ezt a kódot függvénybe úgy, hogy `n`-et argumentumként kapva, adja vissza ezt a mátrixot.
```python
n = int(input("Mekkora legyen a matrix? "))
matrix = matrix_letrehoz(n)
print(n)
```
3. Írj függvényt, mely argumentumként egy ilyen mátrixot kap, és olvashatóan kiírja.
```python
n = int(input("Mekkora legyen a matrix? "))
matrix = matrix_letrehoz(n)
szepen_kiir(n)
```
4. Írj függvényt, mely bekér egy sor és egy oszlop koordinát, valamint egy számot, és ezt beírja a megfelelő pozícióba. 
```python
n = int(input("Mekkora legyen a matrix? "))
matrix = matrix_letrehoz(n)
szepen_kiir(n)
while input("Szeretnel beirni elemet? ") == "igen":
    uj_elemet_beir(matrix)
    szepen_kiir(matrix)
```
5. Írj függvényeket, melyek kimentik, betöltik ezt a mátrixot egy json fájlból.

```python
if input("Uj matrixot szeretnel? ") == "igen":
    n = int(input("Mekkora legyen a matrix? "))
    matrix = matrix_letrehoz(n)
else:
    matrix = matrix_betolt("matrix.json")
szepen_kiir(n)
while input("Szeretnel beirni elemet? ") == "igen":
    uj_elemet_beir(matrix)
    szepen_kiir(matrix)
matrix_kiment(matrix, "matrix.json")
```


