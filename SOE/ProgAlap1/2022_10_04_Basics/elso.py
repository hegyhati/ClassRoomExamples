user_name = input("What's your name? ")
print("Hello "+user_name + "!")

user_age = int(input("How old are you? "))
while user_age < 0 or user_age > 150:
    user_age = int(input("That's impossible, what is your real age? "))

print("Your next birthday will be:", (user_age+1))

if user_age >= 18:
    print("Here: 🍺")
elif user_age <= 3:
    print("Here: 🍼")
else:
    print("Here: 🧋")


print("Bye-bye")
