def fuggveny(lista, szam):
    return szam / 2 in lista


print( "OK" if not fuggveny([1,2,3], 3) else f"Nem OK: [1,2,3], 1")
print( "OK" if fuggveny([1,2,3], 4) else f"Nem OK: [1,2,3], 3")
print( "OK" if not fuggveny([1,2,3], 7) else f"Nem OK: [1,2,3], 7")
print( "OK" if fuggveny([1,2,3], 6) else f"Nem OK: [1,2,3], 5")
print( "OK" if not fuggveny([1,2,4,8,10], 19) else f"Nem OK: [1,2,4,8,10], 19")
print( "OK" if not fuggveny([1,2,4,8,10], -21) else f"Nem OK: [1,2,4,8,10], -21")
print( "OK" if not fuggveny([1,2,4,8,10], 13265) else f"Nem OK: [1,2,4,8,10], 13265")
print( "OK" if fuggveny([1,2,4,8,10], 16) else f"Nem OK: [1,2,4,8,10], 12")
print( "OK" if not fuggveny([], 0) else f"Nem OK: [], 0")