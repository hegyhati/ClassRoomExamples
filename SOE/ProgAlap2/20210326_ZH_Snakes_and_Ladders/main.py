from game import *

board = Board(30)

board.add_jump(27,1)
board.add_jump(21,9)
board.add_jump(19,7)
board.add_jump(17,4)
board.add_jump(3,22)
board.add_jump(5,8)
board.add_jump(11,26)
board.add_jump(20,29)

# play a game with 1 round -> never finishes
impossible_game=Game(board,1)
try:
    winner = impossible_game.simulate_game(['Annie' , 'Betholdt', 'Reiner', 'Marcel'])
    print("The winner is {}".format(winner))
except Exception as e:
    print(e)

# play just one game with statistics
game=Game(board,40)
board.reset_statistics()
try:
    winner = game.simulate_game(['Annie' , 'Betholdt', 'Reiner', 'Marcel'])
    print("The winner is {}".format(winner))
except Exception as e:
    print(e)
board.draw_statistics("1_game.png")


# play a lot of games for better statistics
board.reset_statistics()
for _ in range(9999):
    try:
        winner = game.simulate_game(['Annie' , 'Betholdt', 'Reiner', 'Marcel'])
    except:
        pass
board.draw_statistics("9999_games.png")