from abc import ABC

class Shape(ABC):

    def to_svg(self) -> str: pass
    def area(self) -> float: pass