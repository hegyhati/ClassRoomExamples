import random
from typing import List, Set

def draw() -> List[int]:
    return [ random.randint(1,90) for _ in range(5) ] 

def draw_correct() -> Set[int]:
    numbers = draw()
    while len(set(numbers)) < 5:
        numbers = draw()
    return set(numbers)

def draw_with_set() -> Set[int]:
    numbers = set()
    while len(numbers) < 5:
        numbers.add(random.randint(1,90))
    return numbers

def good(draw:Set[int],guess:Set[int]) -> int:
    return len(draw.intersection(guess))

winner_numbers = draw_correct()

people_guesses = [ draw_correct() for _ in range(100000) ]

goods = [ good(winner_numbers,guess) for guess in people_guesses ]


winners = { key: goods.count(key) for key in range(6) }

print(winners)