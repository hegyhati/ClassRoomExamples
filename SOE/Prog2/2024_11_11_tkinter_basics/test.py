import random
from tkinter import *
from functools import partial

SIZE = 10
MINES =15

mines = set(random.choices([(r,c) for r in range(SIZE) for c in range(SIZE)],k=MINES))

style = {
    "font" : ("Arial", 24)
}

def game_over():
    print("Game over")

def mines_in_neighbors(r:int,c:int) -> int:
    return len(mines.intersection({(r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)}))

def neighbors(r:int, c:int) -> set[tuple[int,int]]:
    return {
        (rr,cc) 
        for (rr,cc) in {(r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)}
        if rr >= 0 and rr < SIZE and cc >=0 and cc < SIZE
    }

def explore(r:int, c:int) -> None:
    global fields_left
    fields_left-=1
    progress_label.configure(text=f"Fields to explore: {fields_left}")
    buttons[r][c].configure(state="disabled", relief="sunken")
    mine_count = mines_in_neighbors(r, c)
    buttons[r][c].configure(text=str(mine_count))
    if mine_count == 0:
        for (rr,cc) in neighbors(r,c):
            if buttons[rr][cc]["state"] != "disabled":
                explore(rr,cc)


def button_click(row:int, col:int):
    print(f"clicked on {row,col}")
    if (row, col) in mines:
        print("BUMM")
        game_over()
        return
    explore(row, col)



fields_left = SIZE ** 2 - MINES

window = Tk()
window.title("My awesome minesweeper")
progress_label = Label(window, text=f"Field to explore: {fields_left}", **style, background="yellow")
mine_field = Frame(window)
Entry(window).pack()



progress_label.pack(fill="both")
mine_field.pack()

buttons : list[list[Button]] = []
for r in range(SIZE):
    buttons.append([])
    for c in range(SIZE):
        b = Button(mine_field,text=" ", command=partial(button_click,r,c), **style)
        buttons[-1].append(b)
        b.grid(row=r, column=c)


window.mainloop()

