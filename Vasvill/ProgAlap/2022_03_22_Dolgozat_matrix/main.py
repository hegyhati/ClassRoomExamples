def matrix_letrehoz(meret):
    lista = []
    for _ in range(meret):
        lista.append([0]*meret)
    return lista

def szepen_kiir(matrix):
    for sor in matrix:
        for elem in sor:
            print(elem, end=' ')
        print()

def uj_elemet_beir(matrix):
    sor = int(input("Melyik sorba? ")) - 1
    oszlop = int(input("Melyik oszlopba? ")) -1 
    szam = int(input("Mit? "))
    matrix[sor][oszlop] = szam


n = int(input("Mekkora legyen a matrix? "))
matrix = matrix_letrehoz(n)
szepen_kiir(matrix)
while input("Szeretnel beirni elemet? ") == "igen":
    uj_elemet_beir(matrix)
    szepen_kiir(matrix)