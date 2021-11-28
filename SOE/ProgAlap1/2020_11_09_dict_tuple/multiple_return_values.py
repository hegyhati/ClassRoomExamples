
def megszamol(lista,szam):
    count=0
    for l in lista:
        if l==szam:
            count+=1
    return count

def leggyakoribbkereses(lista):
    melyik=peldalista[0]
    max=megszamol(peldalista,melyik)
    for l in peldalista:
        db=megszamol(peldalista,l)
        if db > max:
            melyik=l
            max=db
    return (melyik,max)


peldalista=[1,2,2,2,2,3,3,3,3,2,2,2,3,3,4,5,6,7,4,3,2,2,1,23,345,456,45,45,4,52,2,1234,14,1]

(melyik,hanyszor)=leggyakoribbkereses(peldalista)

print("A legtobbszor ",melyik," fordult elo, osszesen ",hanyszor,"alkalommal")


