all_nums = []
has_already = False
num = int(input("Kerem az elso szamot: "))
while not num in all_nums:
    all_nums.append(num)
    num = int(input("Kerek egy szamot: "))

print("A bekert szamok ismetles nelkul: ",all_nums)
