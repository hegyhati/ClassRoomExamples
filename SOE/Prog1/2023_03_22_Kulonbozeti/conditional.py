age = int(input("How old are you? "))
if age >= 18: 
    preference = input("Do you like beers?")
    if preference.lower().strip() == "yes":
        print("Beer!")
    else:
        print("Coca cola")
else:
    print("Milk.")
print("Bye!")
