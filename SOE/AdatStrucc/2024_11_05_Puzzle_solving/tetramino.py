
from block import Block


class Tetramino:

    def __init__(self, blocks:list[tuple[int, int]], id:int) -> None:
        self.__blocks = [Block(*b) for b in blocks]
        self.__id = id
    
    def __str__(self) -> str:
        return f"{self.__id}: {[(b.x, b.y) for b in self.__blocks]}"

    def rotate(self, count:int = 1) -> None:
        for block in self.__blocks:
            block.rotate(count)
    
    def shift(self, dx:int=0, dy:int=0) -> None:
        for block in self.__blocks:
            block.shift(dx,dy)
    
    def mirror(self):
        for block in self.__blocks:
            block.mirror_y()
    
    def min_x(self) -> int:
        return min(block.x for block in self.__blocks)
    def max_x(self) -> int:
        return max(block.x for block in self.__blocks)
    def min_y(self) -> int:
        return min(block.y for block in self.__blocks)
    def max_y(self) -> int:
        return max(block.y for block in self.__blocks)

    def width(self)->int:
        return self.max_x() - self.min_x() + 1
    def height(self)->int:
        return self.max_y() - self.min_y() + 1
    
    def normalize(self):
        self.shift(-self.min_x(), -self.min_y())

    def to_svg(self) -> str:
        return "\n".join([
            block.to_svg(self.id)
            for block in self.__blocks
        ])

    def get_positions(self) -> list[tuple[int,int]]:
        return [ (b.x,b.y)
            for b in self.__blocks
        ]

    def get_id(self) -> int:
        return self.__id

if __name__ == "__main__":
    import json
    with open("tetraminos.json") as f:
        tetraminos = json.load(f)
    tetraminos = [Tetramino(tetramino) for tetramino in tetraminos]
    for id, tetramino in enumerate(tetraminos):
        tetramino.shift(5*(id%4), 5*(id//4))
    
    with open("foo.svg", "w") as f:
        f.write("<svg width=\"2500\" height=\"1000\">")
        for tetramino in tetraminos:
            f.write(tetramino.to_svg())
        f.write("</svg>")



