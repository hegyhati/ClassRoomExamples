import tkinter as tk
from logic import MemoryGame
from functools import partial


class MemoryGameGUI(tk.Tk):
    unknown = "???"

    def __init__(self, width=4, height=5):
        super().__init__()
        if width*height % 2 == 1:
            width += 1
        self.title("Memory game")
        self.game = MemoryGame(width, height)
        self.moveCount = tk.IntVar()
        self.resizable(False, False)

        board = tk.Frame(self)
        self.cards = [[tk.Button(board, width=len(self.unknown), command=partial(
            self.click, w, h), fg="black", disabledforeground="blue") for w in range(width)] for h in range(height)]
        for h in range(height):
            for w in range(width):
                self.cards[h][w].grid(row=h, column=w)
        self.message = tk.StringVar()

        self.messageLabel = tk.Label(self, textvariable=self.message)
        widgets = [
            tk.Label(self, textvariable=self.moveCount),
            board,
            tk.Button(self, text="Reset", command=self.reset),
            self.messageLabel
        ]
        for widget in widgets:
            widget.pack(side="top", fill="x")
        self.reset()

    def reset(self):
        self.last = []
        self.moveCount.set(0)
        self.message.set("")
        self.game.reset()
        for cardrow in self.cards:
            for card in cardrow:
                card.config(text=self.unknown, state="normal", relief="raised")

    def __reveal_card(self, x: int, y: int):
        self.cards[y][x].config(text=self.game.get(x, y), state="disabled")

    def __unturn_card(self, x: int, y: int):
        self.cards[y][x].config(text=self.unknown, state="normal")

    def __keep_card(self, x: int, y: int):
        self.cards[y][x].config(relief="sunken")

    def click(self, x: int, y: int):
        if len(self.last) == 2:
            for (xp, yp) in self.last:
                self.__unturn_card(xp, yp)
                self.last = []
        if len(self.last) == 0:
            self.__reveal_card(x, y)
            self.last = [(x, y)]
        else:
            self.__reveal_card(x, y)
            (xp, yp) = self.last[0]
            if self.game.try_pair(xp, yp, x, y):
                self.__keep_card(xp, yp)
                self.__keep_card(x, y)
                self.last = []
            else:
                self.last.append((x, y))
            self.moveCount.set(self.moveCount.get()+1)
        if self.game.is_won():
            self.messageLabel.config(
                wraplength=self.messageLabel.winfo_width())
            self.message.set(
                f"Congrats, you solved the game in {self.moveCount.get()} steps!")


if __name__ == "__main__":
    ui = MemoryGameGUI(2, 1)
    ui.mainloop()
