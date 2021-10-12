all_nums = []
has_already = False

while not has_already:
    num = int(input("Kerek egy szamot: "))
    has_already = False
    for prev in all_nums:
        if prev == num:
            has_already=True
    if not has_already:
        all_nums.append(num)

print("A bekert szamok ismetles nelkul: ",all_nums)
