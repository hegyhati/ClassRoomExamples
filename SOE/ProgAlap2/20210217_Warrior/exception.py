class OwnException(Exception):
    pass

try:
    print("try eleje")
    raise ArithmeticError
    print("try vege")

except OwnException:
    print("OwnException lekezelese")
except (ZeroDivisionError,FileExistsError):
    print("Zero, filenoutfound lekezelese")
except:
    print("unexpected exception")
else:
    print("else")

try:
    f = open("ize.txt","rt")
except FileNotFoundError:
    print("nincs ize.txt")
else:
    f.close()

try:
    with open("alma.txt") as file:
        print("sikerult aaz almatmegnyitni")
except FileNotFoundError:
    print("nincs alma")
