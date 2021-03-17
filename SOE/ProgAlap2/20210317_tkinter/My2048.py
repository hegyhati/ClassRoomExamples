from tkinter import *
import model


def update():
    global map
    global labels
    global left_button
    for r in range(4):
        for c in range(4):
            labels[r][c].config(text=map[r][c])


def next_step():
    if model.win(map):
        print("Congrats.")
        exit(0)
    elif model.lose(map):
        print("You failed.")
        exit(0)
    model.give_new_2(map)
    update()


def right_clicked():
    global map
    if model.can_list_merge_horizontally(map):
        map = model.move_right(map)
        next_step()


def left_clicked():
    global map
    if model.can_list_merge_horizontally(map):
        map = model.move_left(map)
        next_step()


def up_clicked():
    global map
    if model.can_list_merge_vertically(map):
        map = model.move_up(map)
        next_step()


def down_clicked():
    global map
    if model.can_list_merge_vertically(map):
        map = model.move_down(map)
        next_step()


window = Tk()
board = Frame(window)

labels = []
for r in range(4):
    labels.append([])
    for c in range(4):
        label = Label(board, text="X", bg="gray", width=4,
                      font=("Courier", 24), height=2)
        labels[-1].append(label)
        label.grid(row=r, column=c, padx=5, pady=5)


board.grid(row=1, column=1)
up_button = Button(window, text="↑", bg="blue", font=(
    'Courier', 36), command=up_clicked).grid(row=0, column=1, sticky="we")
down_button = Button(window, text="↓", bg="blue", font=(
    'Courier', 36), command=down_clicked).grid(row=2, column=1, sticky="we")
left_button = Button(window, text="←", bg="blue", font=(
    'Courier', 36), command=left_clicked).grid(row=1, column=0, sticky="ns")
right_button = Button(window, text="→", bg="blue", font=(
    'Courier', 36), command=right_clicked).grid(row=1, column=2, sticky="ns")
window.resizable(False, False)

map = model.set_table()

update()

window.mainloop()
