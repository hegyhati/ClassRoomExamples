import json


def exercise_1_solution_1():
    number = int(input())
    h = number // 100
    t = (number // 10) % 10
    s = number % 10
    print(h+t+s)


def exercise_1_solution_1_general():
    number = int(input())
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    print(sum_digits)


def exercise_1_solution_2():
    number = input()
    print(int(number[0])+int(number[1])+int(number[2]))


def exercise_1_solution_2_general():
    number = input()
    sum_digits = 0
    for digit in number:
        sum_digits += int(digit)
    print(sum_digits)


def exercise_1_solution_2_general_2():
    print(sum([int(d) for d in input()]))


def exercise_2_solution_1():
    words = input()
    word_list = [word.strip() for word in words.split(',')]
    shortest = len(word_list[0])
    for word in word_list:
        if len(word) < shortest:
            shortest = len(word)
    for word in word_list:
        if len(word) == shortest:
            print(word)


def exercise_2_solution_2():
    words = input()
    word_list = [word.strip() for word in words.split(',')]
    shortest = min([len(word) for word in word_list])
    for word in word_list:
        if len(word) == shortest:
            print(word)


def exactly_one(runner1, runner2):
    with open('futok.json') as f:
        runs = json.load(f)
    dates = []
    for run in runs:
        if runner1 in run['runners'] and runner2 not in run['runners']:
            dates.append(run['date'])
        if runner1 not in run['runners'] and runner2 in run['runners']:
            dates.append(run['date'])
    return dates


def exactly_one_2(runner1, runner2):
    with open('futok.json') as f:
        runs = json.load(f)
    dates = []
    for run in runs:
        if runner1 in run['runners'] and runner2 not in run['runners'] or runner1 not in run['runners'] and runner2 in run['runners']:
            dates.append(run['date'])
    return dates


def exactly_one_3(runner1, runner2):
    with open('futok.json') as f:
        runs = json.load(f)
    dates = [
        run['date']
        for run in runs
        if runner1 in run['runners'] and runner2 not in run['runners'] or runner1 not in run['runners'] and runner2 in run['runners']
    ]
    return dates

def exercise_3():
    for r1 in ['D', 'O', 'G']:
        for r2 in ['C', 'A', 'M']:
            print(f"{ len(exactly_one_3(r1,r2)) } db olyan futás volt, ahol {r1} és {r2} közül pontosan az egyik volt ott.")
