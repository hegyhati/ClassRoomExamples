num = -1
sum = 0
all_nums = []
even_nums = []
while num != 0:
    num = int(input("Kerlek adj egy szamot (vege a 0): "))
    all_nums.append(num)
    sum += num
    if num % 2 == 0:
        even_nums.append(num)

print("Osszesen",len(all_nums),"szamot kertunk be, ebbol", len(even_nums), "volt paros")
print("A bekert szamok osszege:",sum)
print("A bekert szamok kozul a parosak:",even_nums)




"""
 4. Eddigi + a vegen irja ki a megadott paros szamokat tartalmazo listat.
"""
