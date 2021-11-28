szam = int(input())

oszto=2
kitevo=0
while szam != 1:
    if szam%oszto != 0:
        print(str(oszto) + "^" + str(kitevo))
        kitevo=0
        while szam%oszto!=0:
            oszto+=1
    szam //= oszto
    kitevo+=1
print(str(oszto) + "^" + str(kitevo))
