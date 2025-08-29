import json


def exercise_1_solution_1():
    number = int(input())
    h = number // 100
    t = (number // 10) % 10
    s = number % 10
    if h >= t and h >= s:
        print(h)
    elif t >= h and t >= s:
        print(t)
    elif s >= t and s >= h:
        print(s)


def exercise_1_solution_2():
    number = int(input())
    h = number // 100
    t = (number // 10) % 10
    s = number % 10
    print(max(h, t, s))


def exercise_1_solution_2_general():
    number = int(input())
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    print(max(digits))


def exercise_1_solution_3():
    number = input()
    print(max(int(number[0]), int(number[1]), int(number[2])))


def exercise_1_solution_3_general():
    print(max([int(d) for d in input()]))


def exercise_1_solution_3_general_2():
    print(max(input()))


def exercise_2_solution_1():
    words = input()
    word_list = [word.strip() for word in words.split(',')]
    longest = len(word_list[0])
    for word in word_list:
        if len(word) > longest:
            longest = len(word)
    for word in word_list:
        if len(word) == longest:
            print(word)


def exercise_2_solution_2():
    words = input()
    word_list = [word.strip() for word in words.split(',')]
    longest = max([len(word) for word in word_list])
    for word in word_list:
        if len(word) == longest:
            print(word)


def ran_together(runner):
    with open('futok.json') as f:
        runs = json.load(f)
    friends = set()
    for run in runs:
        if runner in run['runners']:
            friends.update(run['runners'])
    friends.remove(runner)
    return list(friends)


def exercise_3():
    for r in 'ABCDEFGHIJKLMNO':
        print(f"{r} összesen {len(ran_together(r))} másik futót ismer futásokról.")


exercise_3()
