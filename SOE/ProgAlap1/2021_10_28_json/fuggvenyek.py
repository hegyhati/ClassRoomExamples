def osszead(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def hatvanyoz(alap,kitevo):
    return alap ** kitevo


hatvanyoz(2,3)
hatvanyoz(kitevo=2,alap=3)


if __name__ == "__main__":
    x = int(input("Add meg az elso szamot: "))
    y = int(input("Add meg a masodik szamot: "))
    print("A ket szam osszege:", osszead(x,y))
