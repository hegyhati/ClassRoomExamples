from KlondikeLogic import KlondikeGame
from FrenchDeck import Suit
import pickle
from os.path import join

SAVEDIR = "saves"

ACTIONS = """Action list:
h       turn hand
p       pass waste to hand
r N     reveal the uncovered top of tableau N
f w     move top waste card to foundation
f N     move top card of tableau N to foundation
b N w   build tableau pile N from waste
b N F   build tableau pile N from foundation F
b N M   build tableau pile N from tableau pile M

new     start new game
save F  save to file F
load F  load game state from file F
bye     exit the game
"""


game = KlondikeGame()
print(game)



while not game.is_completed():    
    try: 
        match input("Action:").split():
            case ["h"]: game.turn_hand()
            case ["p"]: game.pass_waste() 
            case ["r", N]: game.reveal_tableau(int(N)-1)
            case ["f", "w"]: game.move_from_waste_to_foundation()
            case ["f", N]: game.move_from_tableau_to_foundation(int(N)-1)
            case ["b", N, "w"]: game.move_from_waste_to_tableau(int(N)-1)
            case ["b", N, F] if F.upper() in [s.name for s in Suit]:
                game.move_from_foundation_to_tableau(Suit[F.upper()],int(N)-1)
            case ["b", N, M]: game.move_from_tableau_to_tableau(int(M)-1,int(N)-1)
            
            case ["new"]: game = KlondikeGame()
            case ["save", filename]: 
                with open(join(SAVEDIR,filename), "wb") as f:
                    pickle.dump(game,f)
                print(f"Game saved to {filename}")
            case ["load", filename]:
                with open(join(SAVEDIR,filename),"rb") as f:
                    game = pickle.load(f)
                print(f"Game loaded from {filename}")
            case ["bye"]: exit()
            case  _: raise ValueError("Unknown action, " + ACTIONS)
    except ValueError as e:
        print("Error", e)
    else:
        print(game)

print("Yaaaaay!")
        
    
    