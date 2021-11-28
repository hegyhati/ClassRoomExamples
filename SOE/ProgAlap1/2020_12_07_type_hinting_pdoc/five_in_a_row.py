from typing import Tuple, List, Dict

player1 = "⨯"
"""Character used for Player 1"""

player2 = "⏺"
"""Character used for Player 2"""

blank = "·"
"""Character used for empty places"""

Position = Tuple[int,int]
"""Type for storing a position. 

The first int is the x coordinate, the second is the y coordinate.
"""

GameState = Dict[str,List[Position]]
"""Type for storing the entire state of the game. 

The key is the string denoting the player. 
The values are lists of Positions that the corresponding player made.
"""

def get_character(moves:GameState, position:Position)->str:
    """Returns the character of a player or blank

    Args:
        moves (GameState): the current state of the game
        position (Position): the position to be checked

    Returns:
        str: player1, player2 or blank
    """
    for player in [player1,player2]:
        for pos in moves[player]:
            if pos==position: return player
    return blank


def is_occupied(moves:GameState,position:Position) -> bool:
    """Checks if a position is already taken or not.

    Args:
        moves (GameState): the current state of the game
        position (Position): the position to be checked

    Returns:
        bool: `True` if the position is already taken, `False` otherwise
    """
    return get_character(moves,position)!=blank

def box(moves:GameState)->Tuple[int,int,int,int]:
    """Returns a box (the smallest one) in which all the previous moves fit into.

    Args:
        moves (GameState): the current state of the game

    Returns:
        Tuple[int,int,int,int]: smallest x coordinate, smallest y coordinate, largest x coordinate,  largest y coordinate. Returns `(0,0,0,0)` if no moves are made yet.
    """
    if len(moves[player1])==0: return (0,0,0,0)
    (minx,miny)=(maxx,maxy)=moves[player1][0]
    for (x,y) in moves[player1]+moves[player2]:
        if x < minx : minx=x
        if x > maxx : maxx=x
        if y < miny : miny=y
        if y > maxy : maxy=y
    return (minx,miny,maxx,maxy)

def print_game(moves:GameState) -> None:
    """Prints out the game state in a simple way.

    Args:
        moves (GameState): the current state of the game
    """
    (minx,miny,maxx,maxy)=box(moves)
    for y in range(miny-1,maxy+2):
        for x in range(minx-1,maxx+2):
            print( get_character(moves,(x,y)), end="" )
        print()



def input_position() -> Position:
    """Reads a position from the input and returns it.

    Returns:
        Position: An `(x,y)` pair of coordinates.
    """
    return (int(input("X position: ")),int(input("Y position: ")))

def make_move(moves:GameState, player:str) -> None:
    """Makes the next move with the given player. 

    Asks for positions until an empty one is given, then inserts it into the current state of the game.

    Args:
        moves (GameState): the current state of the game
        player (str): the character representation of the player
    """
    print("New move for {}:".format(player))
    new_move=input_position()
    while is_occupied(moves,new_move):
        print("Place already taken, provide another position.")
        new_move=input_position()
    print("Thanks")
    moves[player].append(new_move)



def get_position(position:Position, direction:Tuple[int,int], step:int)->Position:
    """Returns a new position, that can be reached from the given position by jumping in the given direction the given times.

    For example, `get_position((14,3),(1,-1),3) -> (17,0)`

    Args:
        position (Position): the base position
        direction (Tuple[int,int]): the direction of the jumps
        step (int): the number of the jumps

    Returns:
        Position: the new position
    """
    return (position[0]+step*direction[0],position[1]+step*direction[1])

def is_five_in_a_row(moves:GameState, position:Position, direction:Tuple[int,int])->bool:
    """Checks whether there are 5 identical marks in a row starting from the given position in the given direction.

    Args:
        moves (GameState): the current state of the game
        position (Position): the position where the check starts
        direction (Tupe[int,int]): the direction, that can be `(1,0)` for right, `(-1,0)` for left, `(0,-1)` for up, etc. 

    Returns:
        bool: `True` if there are 5 identical (non-blank) marks in a row, `False` otherwise
    """
    mark=get_character(moves,position)
    if mark==blank: return False
    for step in range(1,5):
        if get_character(moves,get_position(position,direction,step))!=mark: return False
    return True

def check_win(moves:GameState, player:str)->bool:
    """Checks if `player` had win the game with the last move.

    Args:
        moves (GameState): the current state of the game
        player (str): the character representation of the player

    Returns:
        bool: `True` if `player` has won, `False` otherwise.
    """
    last_move=moves[player][-1]
    for direction in [(0,-1),(1,-1),(1,0),(1,1)]:
        for shift in range(-4,1):
            if is_five_in_a_row(moves,get_position(last_move,direction,shift),direction): return True
    return False


def game():
    """Starts a game until 5 in a row is found, and announces the result.
    """
    moves={player1:[],player2:[]}
    winner=None
    while winner==None:
        for player in [player1,player2]:
            print_game(moves)
            make_move(moves,player)
            if check_win(moves,player):
                winner=player
                break
    print("{} has won the game.".format(winner))
