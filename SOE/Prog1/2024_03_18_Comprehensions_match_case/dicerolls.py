import random

rolls = [random.randint(1,6) for _ in range(1000)]

statistics = {foo: rolls.count(foo) for foo in range(1,7)}
# statistics = {}
# for foo in range(1,7):
#     statistics[foo] = rolls.count(foo)

print(statistics)