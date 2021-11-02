my_list = [ 1, 2, 1, 3, -10, 5, -16, 8, 4, -2, 1, 4, 2, 1 ]

# x bekerese (1 sorbol megoldhato)
x=int(input("Adj egy szamot: "))

# x-nel kisebb pozitiv szamok kiírása (3 sorbol megoldhato)
for elem in my_list:
    if elem < x and x > 0:
        print(elem)


