num = -1
count = 0
sum = 0
count_even = 0
even_nums = []
while num != 0:
    num = int(input("Kerlek adj egy szamot (vege a 0): "))
    count += 1
    sum += num
    if num % 2 == 0:
        count_even += 1
        even_nums.append(num)

print("Osszesen",count,"szamot kertunk be, ebbol", count_even, "volt paros")
print("A bekert szamok osszege:",sum)
print("A bekert szamok kozul a parosak:",even_nums)




"""
 4. Eddigi + a vegen irja ki a megadott paros szamokat tartalmazo listat.
"""
