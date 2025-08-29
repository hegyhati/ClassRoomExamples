all_nums = []
has_already = False

while not has_already:
    num = int(input("Kerek egy szamot: "))
    has_already = num in all_nums
    if not has_already:
        all_nums.append(num)

print("A bekert szamok ismetles nelkul: ",all_nums)
