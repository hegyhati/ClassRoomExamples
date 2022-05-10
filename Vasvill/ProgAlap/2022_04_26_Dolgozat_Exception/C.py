from calendar import c
import json


def exercise_1_solution_1():
    number = int(input())
    h = number // 100
    t = (number // 10) % 10
    s = number % 10
    if h <= t and h <= s:
        print(h)
    elif t <= h and t <= s:
        print(t)
    elif s <= t and s <= h:
        print(s)


def exercise_1_solution_2():
    number = int(input())
    h = number // 100
    t = (number // 10) % 10
    s = number % 10
    print(min(h, t, s))


def exercise_1_solution_2_general():
    number = int(input())
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    print(min(digits))


def exercise_1_solution_3():
    number = input()
    print(min(int(number[0]), int(number[1]), int(number[2])))


def exercise_1_solution_3_general():
    print(min([int(d) for d in input()]))


def exercise_1_solution_3_general_2():
    print(min(input()))


def exercise_2_solution_1():
    vowel_list = ['a', 'á', 'e', 'é', 'i', 'í',
                  'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    words = input().split(',')
    for word in words:
        count = 0
        for character in word:
            if character in vowel_list:
                count += 1
        if count % 2 == 0:
            print(word.strip())


def exercise_2_solution_2():
    vowels = 'öüóúőoiueaéáűí'
    words = input().split(',')
    for word in words:
        count = 0
        for character in word:
            if character in vowels:
                count += 1
        if count % 2 == 0:
            print(word.strip())


def exercise_2_solution_3():
    vowels = 'öüóúőoiueaéáűí'
    words = input().split(',')
    for word in words:
        count = 0
        for vowel in vowels:
            count += word.count(vowel)
        if count % 2 == 0:
            print(word.strip())


def exercise_2_solution_4():
    words = input().split(',')
    for word in words:
        if sum([word.count(vowel) for vowel in 'öüóúőoiueaéáűí']) % 2 == 0:
            print(word.strip())


def exactly_one(runner1, runner2):
    with open('futok.json') as f:
        runs = json.load(f)
    dates = []
    for run in runs:
        if runner1 in run['runners'] and runner2 in run['runners']:
            dates.append(run['date'])
    return dates


def exactly_one_2(runner1, runner2):
    with open('futok.json') as f:
        runs = json.load(f)
    dates = [
        run['date'] for run in runs
        if runner1 in run['runners'] and runner2 in run['runners']
    ]
    return dates


def exercise_3():
    for r1 in ['D', 'O', 'G']:
        for r2 in ['C', 'A', 'M']:
            print(
                f"{r1} és {r2} pontosan { len(together(r1,r2)) } alkalommal futott együtt.")
