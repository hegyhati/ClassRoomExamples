from typing import List, Set, Dict, Tuple, Optional
import random

def give_new_2(map:list) -> None:
    """A function that will put a new 2 in a random location where 0-s are present

    Args:
        map (list): The map that u want to use
    """
    row = random.randint(0,3)
    coluumn = random.randint(0,3)
    while map[row][coluumn] != 0:
        row = random.randint(0,3)
        coluumn = random.randint(0,3)
    map[row][coluumn] = 2

def set_table() -> list:
    """This is the start of everything, this will generate the first table, with a 2 in a random  place

    Returns:
        list: the starting map
    """
    map = []
    for row in range(4):
        rows = [0]*4
        map.append(rows)

    give_new_2(map)

    return map

def win(map:list) -> bool:
    """The function that will check if you have won yet or not

    Args:
        map (list): It will check in this map

    Returns:
        bool: Will give a true if you have won and a false if you haven't won'
    >>> win([[2, 4, 2, 4],[4, 4, 4, 4],[16, 2, 16, 2],[2, 0, 2, 0]])
    False
    >>> win([[2, 4, 16, 64],[256, 16, 4, 16],[256, 512, 1024, 2],[64, 32, 64, 32]])
    False
    >>> win([[4, 4, 4, 4],[4, 4, 4, 4],[4, 4, 4, 4],[2048, 2, 2, 2]])
    True
    """
    for row in map:
        if 2048 in row:
            return True
    return False

def can_list_merge_horizontally(map:list) -> bool:
    """This is used in the lose function and checks if you can merge horizontally or not

    Args:
        map (list): it checks in this map

    Returns:
        bool: Return a True if you can, a false if you can't
    
    >>> can_list_merge_horizontally([[2, 4, 2, 4],[4, 4, 4, 4],[16, 2, 16, 2],[2, 0, 2, 0]])
    True
    >>> can_list_merge_horizontally([[2, 4, 16, 64],[256, 16, 4, 16],[256, 512, 1024, 2],[64, 32, 64, 32]])
    False
    >>> can_list_merge_horizontally([[4, 4, 4, 4],[4, 4, 4, 4],[4, 4, 4, 4],[2048, 2, 2, 2]])
    True
    """
    for row in range(len(map)):
        for coluumn in range(len(map[row])-1):
            if map[row][coluumn] == map[row][coluumn +1]:
                return True
    
    return False

def can_list_merge_vertically(map:list) -> bool:
    """This function checks whether you can merge vertically or not

    Args:
        map (list): The list u want to check

    Returns:
        bool: Rteurn a true if you can a false otherwise
    >>> can_list_merge_vertically([[2, 4, 2, 4],[4, 4, 4, 4],[16, 2, 16, 2],[2, 0, 2, 0]])
    True
    >>> can_list_merge_vertically([[2, 4, 16, 64],[256, 16, 4, 16],[256, 512, 1024, 2],[64, 32, 64, 32]])
    True
    >>> can_list_merge_vertically([[4, 4, 4, 4],[4, 4, 4, 4],[4, 4, 4, 4],[2048, 2, 2, 2]])
    True
    """
    for row in range(len(map)-1):
        for coluumn in range(len(map[row])):
            if map[row][coluumn] == map[row + 1][coluumn]:
                return True
    
    return False

def is_there_zero(map:list) -> bool:
    """This function checks if there is a 0 on the map

    Args:
        map (list): The map u are checking in

    Returns:
        bool: True if there is a 0 on the map and false otherwise
    >>> is_there_zero([[1024, 4, 16, 64],[4, 64, 6, 4],[16, 1024, 16, 512],[2, 32, 2, 1024]])
    False
    >>> is_there_zero([[2, 4, 4, 4],[4, 4, 2, 4],[16, 4, 2, 2],[2, 4, 2, 2]])
    False
    >>> is_there_zero([[2, 4, 2, 2],[0, 4, 2, 4],[2, 2, 2, 2],[4, 4, 2, 2]])
    True
    """
    for row in map:
        if 0 in row:
            return True
    return False

def lose(map:list) -> bool:
    """This function checks if you have lost or not. If there isnt any 0-s and you cant move vertically or horizontally, you have lost

    Args:
        map (list): The map u are checking in

    Returns:
        bool: Return a True if you Lost, a false if you didnt'
    
    >>> lose([[1024, 4, 16, 64],[4, 64, 6, 4],[16, 1024, 16, 512],[2, 32, 2, 1024]])
    True
    >>> lose([[2, 4, 4, 4],[4, 4, 2, 4],[16, 4, 2, 2],[2, 4, 2, 2]])
    False
    >>> lose([[2, 4, 2, 2],[0, 4, 2, 4],[2, 2, 2, 2],[4, 4, 2, 2]])
    False
    """
    return not is_there_zero(map) and not can_list_merge_vertically(map) and not can_list_merge_horizontally(map)

def pull_row_together(row:list) -> list:
    """This function takes 1 list, and pulls all the numbers to the left, and leaving zeros at their place

    Args:
        row (list): the list u want to change

    Returns:
        list: the changed list
    """
    new_row = [0,0,0,0]
    pos = 0
    for number in range(4):
        if row[number] != 0:
            new_row[pos] = row[number]
            pos += 1

    return new_row

def pull_together(map:list) -> list:
    """This function will reutrn a new map, that is basically the same, but has no zeros inbetween the numbers

    Args:
        map (list): The map u are using

    Returns:
        list: The pulled form of the map
    
    >>> pull_together([[2, 0, 0, 4],[4, 0, 0, 4],[16, 0, 0, 2],[2, 0, 2, 0]])
    [[2, 4, 0, 0], [4, 4, 0, 0], [16, 2, 0, 0], [2, 2, 0, 0]]
    >>> pull_together([[2, 0, 0, 4],[4, 0, 2, 4],[16, 0, 2, 2],[2, 0, 2, 2]])
    [[2, 4, 0, 0], [4, 2, 4, 0], [16, 2, 2, 0], [2, 2, 2, 0]]
    >>> pull_together([[2, 0, 2, 2],[0, 0, 2, 4],[0, 0, 2, 2],[0, 0, 2, 2]])
    [[2, 2, 2, 0], [2, 4, 0, 0], [2, 2, 0, 0], [2, 2, 0, 0]]
    """
    new_map = []

    for row in range(len(map)):
        new_row = pull_row_together(map[row])
        new_map.append(new_row)

    return new_map

def merge_row(row:list) -> list:
    """This function will take a list (row) and merges the numbers that are next to each other, to the left side, and will leave a 0 on the right side

    Args:
        row (list): the list u want to change

    Returns:
        list: the changed list
    """
    for number in range(len(row)-1):
        if row[number] != 0 and row[number] == row[number + 1]:
                row[number] *= 2
                row[number + 1] = 0
    return row

def merge(map:list) -> list:
    """It will add the numbers together always in left direction, and will use other functions to get other directions done

    Args:
        map (list): The map u are checking in

    Returns:
        list: The added map
    >>> merge([[4, 4, 4, 4], [4, 4, 4, 4], [0, 0, 0, 0], [2, 2, 2, 2]])
    [[8, 0, 8, 0], [8, 0, 8, 0], [0, 0, 0, 0], [4, 0, 4, 0]]
    >>> merge([[4, 4, 4, 4], [2, 2, 2, 2], [16, 16, 16, 16], [2, 2, 2, 2]])
    [[8, 0, 8, 0], [4, 0, 4, 0], [32, 0, 32, 0], [4, 0, 4, 0]]
    >>> merge([[4, 4, 0, 0], [2, 2, 0, 0], [16, 16, 16, 16], [2, 2, 2, 2]])
    [[8, 0, 0, 0], [4, 0, 0, 0], [32, 0, 32, 0], [4, 0, 4, 0]]
    """
    new_map = []
    for row in range(len(map)):
        new_row = merge_row(map[row])
        new_map.append(new_row)

    return new_map


def reverse(map:list) -> list:
    """
    This will reverse the map

    Args:
        map (list): The map u are reversing

    Returns:
        list: The reversed version of map
    >>> reverse([[0, 0, 2, 2], [0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]])
    [[2, 2, 0, 0], [2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> reverse([[2, 0, 2, 2], [2, 0, 2, 2], [16, 0, 4, 2], [2, 0, 16, 0]])
    [[2, 2, 0, 2], [2, 2, 0, 2], [2, 4, 0, 16], [0, 16, 0, 2]]
    >>> reverse([[2, 0, 0, 0], [0, 0, 0, 2], [16, 0, 0, 0], [2, 0, 0, 0]])
    [[0, 0, 0, 2], [2, 0, 0, 0], [0, 0, 0, 16], [0, 0, 0, 2]]
    """
    new_map = []
    for row in range(4):
        new_map.append([])
        for coluumn in range(4):
            new_map[row].append(map[row][3-coluumn])

    return new_map

def transpose(map:list) -> list:
    """This will interchange the maps coluumns and rows

    Args:
        map (list): The map u are interchaning

    Returns:
        list: The interchanged version of the map
    >>> transpose([[2, 2, 0, 2], [2, 2, 0, 2], [2, 2, 0, 2], [2, 2, 0, 0]])
    [[2, 2, 2, 2], [2, 2, 2, 2], [0, 0, 0, 0], [2, 2, 2, 0]]
    >>> transpose([[0, 2, 0, 2], [0, 2, 0, 2], [0, 0, 0, 2], [2, 0, 0, 2]])
    [[0, 0, 0, 2], [2, 2, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2]]
    >>> transpose([[0, 16, 0, 2], [0, 16, 0, 2], [16, 0, 0, 2], [2, 0, 0, 2]])
    [[0, 0, 16, 2], [16, 16, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2]]
    """
    new_map = []
    for row in range(4):
        new_map.append([])
        for coluumn in range(4):
            new_map[row].append(map[coluumn][row])
    
    return new_map


def score(map:list) -> int:
    """The function that calculates the score that the player has. First it calculates every number that is on the table, than the value gets multiplied by 10

    Args:
        map (list): The map

    Returns:
        int: The claculated score
    """
    allscore = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            tempscore = map[i][j] * 10
            allscore += tempscore
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1024:
                allscore += 500
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 2048:
                allscore += 1000
                
    return allscore

def move_left(map:list) -> list:
    """The function to handle the left moving command. First u pull the map together, than add the numbers, then pull again

    Args:
        map (list): the map u want to change

    Returns:
        list: the changed map

    >>> move_left([[16, 16, 4, 4], [8, 4, 4, 4], [16, 16, 4, 4], [16, 0, 2, 0]])
    [[32, 8, 0, 0], [8, 8, 4, 0], [32, 8, 0, 0], [16, 2, 0, 0]]
    >>> move_left([[16, 16, 4, 4], [4, 4, 4, 4], [16, 16, 2, 4], [16, 2, 2, 0]])
    [[32, 8, 0, 0], [8, 8, 0, 0], [32, 2, 4, 0], [16, 4, 0, 0]]
    >>> move_left([[16, 16, 64, 64], [16, 16, 4, 4], [32, 32, 2, 4], [16, 2, 2, 0]])
    [[32, 128, 0, 0], [32, 8, 0, 0], [64, 2, 4, 0], [16, 4, 0, 0]]
    """
    new_map = pull_together(map)
    new_map = merge(new_map)
    new_map = pull_together(new_map)
    return new_map


def move_right(map:list) -> list:
    """The function to handle when u want to move right. First u reverse the map, then u use the move left function, that u reverse again to get the default map

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed version of the map

    >>> move_right([[0, 0, 4, 4], [0, 0, 4, 4], [0, 16, 0, 4], [0, 0, 2, 0]])
    [[0, 0, 0, 8], [0, 0, 0, 8], [0, 0, 16, 4], [0, 0, 0, 2]]
    >>> move_right([[16, 0, 4, 4], [8, 0, 4, 4], [0, 16, 4, 4], [16, 0, 2, 0]])
    [[0, 0, 16, 8], [0, 0, 8, 8], [0, 0, 16, 8], [0, 0, 16, 2]]
    >>> move_right([[16, 16, 4, 4], [8, 4, 4, 4], [16, 16, 4, 4], [16, 0, 2, 0]])
    [[0, 0, 32, 8], [0, 8, 4, 8], [0, 0, 32, 8], [0, 0, 16, 2]]
    """
    new_map = reverse(map)
    new_map = move_left(new_map)
    new_map = reverse(new_map)
    return new_map


def move_up(map:list) -> list:
    """The function that handles the up command. First u interchang the map, than u move left, than u interchange again to get the default map

    Args:
        map (list): The map u want to change

    Returns:
        list: The changed map

    >>> move_up([[16, 16, 64, 64], [16, 16, 4, 4], [32, 32, 2, 4], [16, 2, 2, 0]])
    [[32, 32, 64, 64], [32, 32, 4, 8], [16, 2, 4, 0], [0, 0, 0, 0]]
    >>> move_up([[16, 16, 64, 64], [16, 16, 4, 64], [32, 32, 2, 4], [32, 2, 2, 4]])
    [[32, 32, 64, 128], [64, 32, 4, 8], [0, 2, 4, 0], [0, 0, 0, 0]]
    >>> move_up([[64, 16, 64, 64], [64, 16, 4, 64], [124, 32, 2, 4], [124, 2, 2, 4]])
    [[128, 32, 64, 128], [248, 32, 4, 8], [0, 2, 4, 0], [0, 0, 0, 0]]
    """
    new_map = transpose(map)
    new_map = move_left(new_map)
    new_map = transpose(new_map)
    return new_map

def move_down(map:list) -> list:
    """The function that handles the move down command, nfirst u interchange the map, than u move right, than u interchange again to get the default map

    Args:
        map (list): the map u want to change

    Returns:
        list: The changed map
    >>> move_down([[64, 16, 64, 4], [64, 16, 4, 4], [124, 32, 2, 4], [124, 2, 4, 4]])
    [[0, 0, 64, 0], [0, 32, 4, 0], [128, 32, 2, 8], [248, 2, 4, 8]]
    >>> move_down([[64, 16, 64, 4], [124, 16, 4, 4], [124, 32, 2, 4], [124, 2, 4, 4]])
    [[0, 0, 64, 0], [64, 32, 4, 0], [124, 32, 2, 8], [248, 2, 4, 8]]
    >>> move_down([[64, 16, 64, 4], [124, 16, 4, 4], [124, 32, 2, 4], [124, 32, 4, 4]])
    [[0, 0, 64, 0], [64, 0, 4, 0], [124, 32, 2, 8], [248, 64, 4, 8]]
    """
    new_map = transpose(map)
    new_map = move_right(new_map)
    new_map = transpose(new_map)
    return new_map
