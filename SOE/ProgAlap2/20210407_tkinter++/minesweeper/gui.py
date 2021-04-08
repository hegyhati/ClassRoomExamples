import logic
from tkinter import *
from functools import partial


def reset():
    global board
    global moves
    board = logic.make_board(size,bombs)
    logic.assign_values(board)
    moves=[]
    for r in range(size):
        for c in range(size):
            fields[r][c].config(text=" ", state=NORMAL, relief=RAISED)
    game_frame.pack(side="top")
    status_label.config(text="Game active")

def update(all=False):
    for r in range(size):
        for c in range(size):
            if((r,c) in moves or all):
                fields[r][c].config(text=str(board[r][c]) if board[r][c]!=0 else " ", state=DISABLED, relief=SUNKEN)

def field_clicked(row,column):
    if board[row][column]=="*":
        status_label.config(text="You loose")
        update(all=True)
    else:    
        logic.dig(board,moves,(row,column))
        if len(moves) == (size**2 - bombs):
            status_label.config(text="You WIN")
            update(all=True)
        else:
            update()


size = 20
bombs = 15


window = Tk()

top_frame = Frame(window)
game_frame = Frame(window)

reset_button = Button(top_frame, text = "Reset", command=reset)
status_label = Label(top_frame)
reset_button.pack(side="left")
status_label.pack(side="left")
top_frame.pack(side="top")

fields=[]
for r in range(size):
    fields.append([])
    for c in range(size):
        field = Button(game_frame, width=1, command=partial(field_clicked,r,c), disabledforeground="blue")
        fields[-1].append(field)
        field.grid(row=r, column=c)
game_frame.pack(side="top")

board = None
moves = None

reset()


window.mainloop()
