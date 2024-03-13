familyname = input("Vezeteknev: ")
firstname = input("Keresztnev: ")
age = int(input("Kor: "))

print(familyname[0]+". "+firstname+" ("+str(age)+")")
print("{}. {} ({})".format(familyname[0], firstname, age))
print(f"{familyname[0]}. {firstname} ({age})")


