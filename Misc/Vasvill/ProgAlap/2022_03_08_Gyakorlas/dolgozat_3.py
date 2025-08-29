numbers_with_commas = input()
number_list = numbers_with_commas.split('')

for number in number_list:
    for number2 in number_list:
        if int(number) + int(number2) == 100:
            print(f"{number} + {number2} = 100")