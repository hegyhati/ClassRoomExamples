my_list = [ 1, 2, 1, 3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1 ]
# x bekerese (1 sorbol megoldhato)
x = int(input("Kerem a szamot: "))

# x es duplaja kozotti szamok kiirasa (3 sorbol megoldhato)
for kiscica in my_list:
    if kiscica > x and kiscica <= 2*x:
        print(kiscica)


