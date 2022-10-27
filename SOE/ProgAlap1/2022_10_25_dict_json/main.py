import json

with open("harry_potter.json") as file:
    figurines = json.load(file)

figurines.append({
    "name":  input("Kinek a karakteret vetted meg? "),
    "house":  input("Melyik hazba tartozik? "),
    "material":  input("Milyen anyagbol keszult a figura? "),
    "size": int(input("Milyen magas a figura? "))
})

with open("harry_potter.json", "w") as file:
    json.dump(figurines, file, indent=4)
