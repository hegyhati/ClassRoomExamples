from dataclasses import dataclass
from colors import colors

@dataclass
class Block:
    x:int = 0
    y:int = 0


    def __rotate_90_counterclockwise(self) -> None:
        self.x, self.y = -self.y, self.x

    def rotate(self, count:int = 1) -> None:
        for _ in range(count):
            self.__rotate_90_counterclockwise()
    
    def shift(self, dx:int=0, dy:int=0) -> None:
        self.x += dx
        self.y += dy
    
    def mirror_y(self) -> None:
        self.x *= -1
    
    def __iadd__(self, d : tuple[int,int]):
        self.shift(*d)
        return self

    def to_svg(self, color:int = 0) -> str:

        return f'<rect width="100" height="100" x="{100*self.x}" y="{100*self.y}" fill="{colors[color]}" />'


if __name__ == "__main__":
    b = Block(1,2)
    b.rotate()
    b += (10,10)
    print(b)
    print(b.to_svg())