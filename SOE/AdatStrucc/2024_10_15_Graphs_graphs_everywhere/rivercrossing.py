from enum import Enum
from copy import deepcopy

class Side(Enum):
    LEFT = 1
    RIGHT = 2

def other(side:Side):
    if side == Side.LEFT : return Side.RIGHT
    else: return Side.LEFT

class Person(Enum):
    MAN = "M"
    BOY = "m"
    WOMAN = "W"
    GIRL = "w"
    SHERIF = "S"
    KILLER = "K" 

BIGPERSON = {Person.MAN, Person.WOMAN, Person.SHERIF}

start_state = {
    Side.LEFT : {
        Person.MAN : 1,
        Person.BOY : 2,
        Person.WOMAN : 1,
        Person.GIRL : 2,
        Person.SHERIF : 1,
        Person.KILLER : 1        
    },    
    Side.RIGHT : {
        Person.MAN : 0,
        Person.BOY : 0,
        Person.WOMAN : 0,
        Person.GIRL : 0,
        Person.SHERIF : 0,
        Person.KILLER : 0        
    },
    "boat" : Side.LEFT
}
end_state = {
    Side.RIGHT : start_state[Side.LEFT],    
    Side.LEFT : start_state[Side.RIGHT],
    "boat" : other(start_state["boat"])
}

def state_string(state:dict) -> None:
    result = []
    for key,value in state[Side.LEFT].items():
        result.append(key.value * value)
    result.append( "\\__/ ||     " if state['boat'] == Side.LEFT else "     || \\__/")
    for key,value in state[Side.RIGHT].items():
        result.append(key.value * value)
    return "".join(result)
        
def only_big_person_moves(state:dict, person:Person) -> dict | None:
    if person not in BIGPERSON: raise ValueError
    current = state["boat"]
    next = other(current)
    if state[current][person] == 1:
        next_state = deepcopy(state)
        next_state["boat"] = next
        next_state[current][person] -= 1
        next_state[next][person] += 1
        return next_state

def two_person_moves(state:dict, big_person:Person, other_person:Person) -> dict | None:
    if big_person not in BIGPERSON: raise ValueError
    if big_person == other_person: raise ValueError
    current = state["boat"]
    next = other(current)
    if state[current][big_person] == 1 and state[current][other_person] > 0:
        next_state = deepcopy(state)
        next_state["boat"] = next
        next_state[current][big_person] -= 1
        next_state[next][big_person] += 1
        next_state[current][other_person] -= 1
        next_state[next][other_person] += 1
        return next_state


def nok_killer(state_side:dict) -> bool:
    return state_side[Person.KILLER] == 1 and state_side[Person.SHERIF] == 0 and (
        state_side[Person.MAN] > 0 or
        state_side[Person.WOMAN] > 0 or
        state_side[Person.BOY] > 0 or
        state_side[Person.GIRL] > 0        
    )

def nok_man(state_side:dict) -> bool:
    return state_side[Person.MAN] == 1 and state_side[Person.WOMAN] == 0 and state_side[Person.GIRL] > 0

def nok_woman(state_side:dict) -> bool:
    return state_side[Person.MAN] == 0 and state_side[Person.WOMAN] == 1 and state_side[Person.BOY] > 0

def ok_state(state:dict) -> bool:
    for side in Side:
        for nok in {nok_man, nok_woman, nok_killer}:
            if nok(state[side]): return False
    return True

def neighbors(state:dict) -> list[dict]:
    neighbor_list = []
    for person in BIGPERSON:
        next_state = only_big_person_moves(state, person)
        if not next_state is None and ok_state(next_state):
            neighbor_list.append(next_state)
    for (big_person, other_person) in {
        (Person.MAN, Person.WOMAN),
        (Person.MAN, Person.SHERIF),
        (Person.MAN, Person.BOY),
        (Person.WOMAN, Person.SHERIF),
        (Person.WOMAN, Person.GIRL),
        (Person.SHERIF, Person.KILLER),
        (Person.SHERIF, Person.BOY),
        (Person.SHERIF, Person.GIRL)
    }:
        next_state = two_person_moves(state, big_person, other_person)
        if not next_state is None and ok_state(next_state):
            neighbor_list.append(next_state)
    return neighbor_list




class FoundItException(Exception):
    pass

visited = {}

def find_vertex(source:dict, target:dict) -> None:
    if source == target: raise FoundItException("Yeppee")
    for neighbor in neighbors(source):
        if state_string(neighbor) not in visited:
            visited[state_string(neighbor)] = source
            find_vertex(neighbor,target)
        
try:
    visited[state_string(start_state)] = None
    find_vertex(start_state,end_state)
except FoundItException as e:
    current = end_state
    while current != start_state:
        print(state_string(current))
        current = visited[state_string(current)]
    print(state_string(start_state))

