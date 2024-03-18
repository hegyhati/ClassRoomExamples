legs = int(input("Hany laba van az allatnak?"))

# if legs == 4:
#     print("Negylabu")
# elif legs == 2:
#     print("MADAR!!!!")
# elif legs == 0:
#     print("Slytherin ftw")
# else:
#     print("Tanulj meg szamolni.")

match legs:
    case 4:
        print("Negylabu")
    case 2:
        print("MADAR!!!!")
    case 0:
        print("Slytherin ftw")
    case other:
        print("Tanulj meg szamolni")
       