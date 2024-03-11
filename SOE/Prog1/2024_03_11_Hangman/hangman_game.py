import hangman_logic as logic
import hangman_ui as ui

gs = logic.get_initial_gamestate()

while not logic.game_ended(gs):    
    ui.print_game_state(gs)
    guess = ui.input_new_guess(gs)
    ui.guess_response(gs, logic.apply_guess(gs, guess))
        
ui.good_bye_message(gs)