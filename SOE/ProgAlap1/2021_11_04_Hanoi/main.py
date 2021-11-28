import model
import ui

if __name__ == "__main__":
    state = model.initial_state()
    while not model.win(state):
        ui.display(state)
        move = ui.get_move()
        if model.good(state, move):
            model.apply(state, move)
        else:
            print("Nem jo lepes!")
    print("Congrats!")
    ui.display(state)
