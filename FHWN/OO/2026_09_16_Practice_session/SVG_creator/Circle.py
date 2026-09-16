from Point import *
from Shape import *

class Circle(Shape):
    __center: Point
    __radius: float
    __color: str

    def __init__(self, center:Point, radius:float, color:str = "black"):
        self.__center = center
        self.__radius = radius
        self.__color = color
        
    def area(self) -> float:
        return self.__radius ** 2 * 3.141521

    def to_svg(self) -> float:
        return f'<circle cx="{self.__center.x}" cy="{self.__center.y}" r="{self.__radius}" fill="{self.__color}" />'


