from Point import *
from Shape import *

class Rectangle(Shape):
    __topleft: Point
    __bottomright: Point
    __color: str

    def __init__(self, p1:Point, p2:Point, color:str = "black"):
        self.__topleft = Point(
            min(p1.x,p2.x),
            min(p1.y,p2.y)            
        )
        self.__bottomright = Point(
            max(p1.x,p2.x),
            max(p1.y,p2.y)            
        )
        self.__color = color

    def width(self) -> float:
        return self.__bottomright.x - self.__topleft.x

    def height(self) -> float:
        return self.__bottomright.y - self.__topleft.y

    def area(self) -> float:
        return self.width() * self.height()

    def to_svg(self) -> float:
        return f'<rect x="{self.__topleft.x}" y="{self.__topleft.y}" width="{self.width()}" height="{self.height()}" fill="{self.__color}" />'


class Square (Rectangle) :
    def __init__(self, topleft:Point, size:float, color = "black"):
        super().__init__(topleft, Point(topleft.x+size, topleft.y+size), color)