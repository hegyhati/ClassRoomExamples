my_list = [ 1, 2, 1, 3, -10, 5, -16, 8, 4, -2, 1, 4, 2, 1 ]
# x bekerese (1 sorbol megoldhato)
x=int(input("Kerek egy szamot: "))

# yeppeee! kiirasa ahanyszor x szerepel (3 sorbol megoldhato)
for elem in my_list:
    if elem == x:
        print("yeppeee!")

