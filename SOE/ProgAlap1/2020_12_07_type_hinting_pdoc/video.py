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
    pass


def is_occupied(moves:GameState,position:Position) -> bool:
    """Checks if a position is already taken or not.

    Args:
        moves (GameState): the current state of the game
        position (Position): the position to be checked

    Returns:
        bool: `True` if the position is already taken, `False` otherwise
    """
    pass

def box(moves:GameState)->Tuple[int,int,int,int]:
    """Returns a box (the smallest one) in which all the previous moves fit into.

    Args:
        moves (GameState): the current state of the game

    Returns:
        Tuple[int,int,int,int]: smallest x coordinate, smallest y coordinate, largest x coordinate,  largest y coordinate. Returns `(0,0,0,0)` if no moves are made yet.
    """
    pass       

def print_game(moves:GameState) -> None:
    """Prints out the game state in a simple way.

    Args:
        moves (GameState): the current state of the game
    """
    pass


def input_position() -> Position:
    """Reads a position from the input and returns it.

    Returns:
        Position: An `(x,y)` pair of coordinates.
    """
    pass

def make_move(moves:GameState, player:str) -> None:
    """Makes the next move with the given player. 

    Asks for positions until an empty one is given, then inserts it into the current state of the game.

    Args:
        moves (GameState): the current state of the game
        player (str): the character representation of the player
    """
    pass

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
    pass

def is_five_in_a_row(moves:GameState, position:Position, direction:Tuple[int,int])->bool:
    """Checks whether there are 5 identical marks in a row starting from the given position in the given direction.

    Args:
        moves (GameState): the current state of the game
        position (Position): the position where the check starts
        direction (Tupe[int,int]): the direction, that can be `(1,0)` for right, `(-1,0)` for left, `(0,-1)` for up, etc. 

    Returns:
        bool: `True` if there are 5 identical (non-blank) marks in a row, `False` otherwise
    """
    pass

def check_win(moves:GameState, player:str)->bool:
    """Checks if `player` had win the game with the last move.

    Args:
        moves (GameState): the current state of the game
        player (str): the character representation of the player

    Returns:
        bool: `True` if `player` has won, `False` otherwise.
    """
    pass


def game():
    """Starts a game until 5 in a row is found, and announces the result.
    """
    pass      
