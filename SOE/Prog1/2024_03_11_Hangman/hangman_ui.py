import hangman_language_loader
import hangman_logic as logic

literals = None

def input_new_guess(gs:dict) -> str:
    print()
    while True:
        guess = input(literals["NEXT GUESS"]+" ").lower()
        if logic.valid_guess(gs, guess):
            break
        print(literals["INVALID GUESS"], end="")
    return guess
   
def print_game_state(gs:dict) -> None:
    print("━"*40)
    print(" ".join(logic.get_clue(gs)))
    print(literals["HISTORY"] +": " + ', '.join(gs['previous']))
    print(literals["LIFE"]+ ": " + '♡' * gs['life'] + '☠' * (logic.MAX_LIFE-gs['life']))
    print("━"*40)
    print()
    
def select_language() -> None:
    global literals
    languages = hangman_language_loader.available_languages()
    while True:
        lang = input(" / ".join(languages)+"  ").lower()
        if lang in languages:
            literals = hangman_language_loader.load_language(lang)
            return

def guess_response(gs:dict, good: bool) -> None:
    print(literals["GOOD GUESS" if good else"BAD GUESS"])

def good_bye_message(gs:dict) -> None:
    print_game_state(gs)
    if logic.game_over(gs):
        print(literals["GAME OVER"])
    if logic.win_check(gs):
        print(literals["CONGRATS"])
        
select_language()