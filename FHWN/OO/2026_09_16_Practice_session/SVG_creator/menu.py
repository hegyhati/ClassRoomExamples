from Rectangle import *
from Circle import *
from Shape import *
from random import choice


colors = ["red", "blue", "green"]

shapes:list[Shape] = []

while True:
    selection = int(input("""
    What do you want to do?
        1. Add a circle
        2. Add a square
        3. save the SVG & exit
        """))
    match selection:
        case 1: 
            x = float(input("x = "))
            y = float(input("y = "))
            r = float(input("r = "))
            shapes.append(Circle(Point(x,y),r,choice(colors)))
        case 2:
            x = float(input("x = "))
            y = float(input("y = "))
            a = float(input("a = "))
            shapes.append(Square(Point(x,y),a,choice(colors)))
        case 3: 
            filename = input("Filename: ")
            with open(f"{filename}.svg","w") as f:
                f.write('<svg height="100" width="100" xmlns="http://www.w3.org/2000/svg">\n')
                for shape in shapes:
                    f.write(shape.to_svg() + "\n")
                f.write("</svg>")   
            break