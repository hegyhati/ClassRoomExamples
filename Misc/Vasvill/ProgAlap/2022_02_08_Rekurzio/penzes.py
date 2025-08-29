ermek = [5, 10, 20, 50, 100, 200]


def hanyfelekeppen(osszeg):
    if osszeg < 0:
        return None
    if osszeg == 0:
        return [[]]
    modok = []
    for erme in ermek:
        kisebbmodok = hanyfelekeppen(osszeg-erme)
        if kisebbmodok != None:
            for mod in kisebbmodok:
                modok.append(mod[:] + [erme] )
    return modok


for mod in hanyfelekeppen(35):
    print(mod)