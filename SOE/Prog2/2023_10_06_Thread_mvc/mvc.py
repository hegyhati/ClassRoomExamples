"""
Model - View - Controller

User interaction -> Controller

controller:
 - model, do your thing
 - hey view, update yourself
    - view: hey model, tell me this and that
"""


class TickTackToe_Model:
    players = "XO"
    def __init__(self) -> None:
        self.table = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.next = 0
    def move(self,x,y):
        if self.table[x][y] == " ":
            self.table[x][y] = self.players[self.next]
            self.next = 1-self.next
    
    def get(self, x,y):
        return self.table[x][y]

    def check_win(self): 
        return False

    def check_ended(self):
        return False

class TickTackToe_TextView:
    def __init__(self, model) -> None:
        self.model = model
    
    def update(self):
        for y in range(3):
            for x in range(3):
                if x > 0: print("|", end="")
                print(self.model.get(x,y), end="")
            print()
            if y < 2: print("-+-+-")

class TickTackToe_SVGView:
    def __init__(self, model, filename) -> None:
        self.model = model
        self.filename = filename
        self.update()

    def update(self):
        with open(self.filename, "w") as file:
            file.write('<svg width="300" height="300">')
            file.write('  <line x1="100" y1="0" x2="100" y2="300" stroke="black" stroke-width="5" />')
            file.write('  <line x1="200" y1="0" x2="200" y2="300" stroke="black" stroke-width="5" />')
            file.write('  <line x1="0" y1="100" x2="300" y2="100" stroke="black" stroke-width="5" />')
            file.write('  <line x1="0" y1="200" x2="300" y2="200" stroke="black" stroke-width="5" />')
            for x in range(3):
                for y in range(3):
                    if self.model.get(x,y) == "O":
                        file.write(f'    <circle cx="{x*100+50}" cy="{y*100+50}" r="40" stroke="blue" stroke-width="3" />')
                    if self.model.get(x,y) == "X":
                        file.write(f'  <line x1="{x*100+10}" y1="{y*100+10}" x2="{x*100+90}" y2="{y*100+90}" stroke="black" stroke-width="5" />')
                        file.write(f'  <line x1="{x*100+10}" y1="{y*100+90}" x2="{x*100+90}" y2="{y*100+10}" stroke="black" stroke-width="5" />')

            file.write("</svg>")



model = TickTackToe_Model()
view = TickTackToe_TextView(model)
view2 = TickTackToe_SVGView(model,"ticktacktoe.svg")
view.update()

while not model.check_ended():
    move = input("Kovetkezo lepes? ")
    x,y = (int(m) for m in move.split(","))
    model.move(x,y)
    view.update()
    view2.update()
    

