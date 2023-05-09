try:
    print("Try")
    Error = input()
    match(Error):
        case "v" : raise ValueError
        case "i" : raise IndexError
        case "n" : raise NameError
    print("Try end")
except ValueError:
    print("ValueError")
else:
    print("Else")
finally:
    print("Finally")
print("End")