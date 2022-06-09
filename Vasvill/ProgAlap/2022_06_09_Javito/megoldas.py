def fuggveny(lista,szam):
    for egyik in lista:
        for masik in lista:
            if egyik + masik == szam:
                return True
    return False

# A fenti elfogadja azt is, hogy ugyanazt az elemet vesszuk ketszer. Egy megoldas, ami ezt kikeruli:

def fuggveny2(lista, szam):
    for i in range(len(lista)):
        for j in range(j+1,len(lista)):
            if lista[i]+lista[j]==szam:
                return True
    return False

print( "OK" if not fuggveny([1,2,3], 1) else f"Nem OK: [1,2,3], 1")
print( "OK" if fuggveny([1,2,3], 3) else f"Nem OK: [1,2,3], 3")
print( "OK" if not fuggveny([1,2,3], 7) else f"Nem OK: [1,2,3], 7")
print( "OK" if fuggveny([1,2,3], 5) else f"Nem OK: [1,2,3], 5")
print( "OK" if not fuggveny([1,2,4,8,10], 19) else f"Nem OK: [1,2,4,8,10], 19")
print( "OK" if not fuggveny([1,2,4,8,10], -21) else f"Nem OK: [1,2,4,8,10], -21")
print( "OK" if not fuggveny([1,2,4,8,10], 13265) else f"Nem OK: [1,2,4,8,10], 13265")
print( "OK" if fuggveny([1,2,4,8,10], 12) else f"Nem OK: [1,2,4,8,10], 12")
print( "OK" if not fuggveny([], 0) else f"Nem OK: [], 0")