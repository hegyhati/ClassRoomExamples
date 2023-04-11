import random

def ask_for_number(text):
    number = input(text + " ")
    while not number.isdecimal():
        number = input("Szamot adj meg: ")
    return int(number)

def roll_sum(count):
    sum = 0
    for _ in range(count):
        sum += random.randint(1,6)
    return sum

def run_experiment(roll_count, repetition):
    values = []
    for _ in range(repetition):
        values.append(roll_sum(roll_count))
    return values

def get_distribution(values):
    count = {}
    for value in set(values):
        count[value] = numbers.count(value)
    return count

def plot_distribution(distribution, max_width=100):
    max_occurance = max(distribution.values())
    for sum,occurance in distribution.items():
        print(f"{sum:>4}: ", end='')
        print("█"*((max_width*occurance)//max_occurance))


roll_count = ask_for_number("Hany dobokocka dobas osszeget nezzuk?")
repetition = ask_for_number("Hanyszor hajtsuk vegre a kiserletet?")

numbers = run_experiment(roll_count, repetition)

distribution = get_distribution(numbers)

plot_distribution(distribution)


