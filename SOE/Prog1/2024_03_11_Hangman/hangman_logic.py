import json
import random

SECRET_CHARACTERS = {chr(c) for c in range(ord("a"), ord("z")+1)}
HIDE_CHARACTER = "_"
MAX_LIFE = 5

def get_initial_gamestate() -> dict:
    with open("puzzles.json") as f:
        puzzles = json.load(f)
    return {
        "secret" : random.choice(puzzles),
        "life" : MAX_LIFE,
        "previous" : set()
    }

def is_revealed(gs:dict, c:str) -> bool:
    return c.lower() not in SECRET_CHARACTERS or c.lower() in gs["previous"]

def win_check(gs:dict) -> bool:
    for char in gs["secret"]:
        if not is_revealed(gs,char): return False
    return True

def game_ended(gs:dict) -> bool:
    return win_check(gs) or game_over(gs)

def game_over(gs:dict) -> bool:
    return gs["life"] == 0

def valid_guess(gs:dict, guess:str) -> bool:
    if len(guess) != 1: return False
    if guess not in SECRET_CHARACTERS: return False
    if guess in gs["previous"]: return False
    return True

def get_clue(gs:dict) -> list:
    return [
        char if is_revealed(gs,char) else HIDE_CHARACTER 
        for char in gs["secret"]
    ]

def apply_guess(gs:dict, guess:str) -> bool:
    guess = guess.lower()
    if not valid_guess(gs, guess) : return # ... 3 weeks from now... 
    gs["previous"].add(guess)
    if guess not in gs["secret"].lower():
        gs["life"] -= 1
        return False
    return True
        