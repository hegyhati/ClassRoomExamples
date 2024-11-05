import json
from copy import deepcopy
from block import Block


class Tetramino:

    __next_color_id = -1

    @classmethod
    def __get_next_color_id(cls):
        cls.__next_color_id += 1
        return cls.__next_color_id

    def __init__(self, blocks:list[tuple[int, int]], mirrorable:bool = True, unique_rotations:tuple[int]|None = None, color_id:int|None = None) -> None:        
        if unique_rotations is None: unique_rotations = (1,2,3,4)
        if color_id is None: color_id = self.__get_next_color_id()

        self.__blocks = tuple(Block(*b) for b in blocks)
        self.__mirrorable = mirrorable
        self.__unique_rotations = unique_rotations
        self.__color_id = color_id

    
    def __str__(self) -> str:
        return f"{self.__color_id}: {[(b.x, b.y) for b in self.__blocks]}"

    def rotate(self, count:int = 1) -> "Tetramino":
        for block in self.__blocks:
            block.rotate(count)
        return self
    
    def shift(self, dx:int=0, dy:int=0) -> "Tetramino":
        for block in self.__blocks:
            block.shift(dx,dy)
        return self
    
    def mirror(self) -> "Tetramino":
        for block in self.__blocks:
            block.mirror_y()
        return self
    
    def min_x(self) -> int:
        return min(block.x for block in self.__blocks)
    def max_x(self) -> int:
        return max(block.x for block in self.__blocks)
    def min_y(self) -> int:
        return min(block.y for block in self.__blocks)
    def max_y(self) -> int:
        return max(block.y for block in self.__blocks)

    def width(self) -> int:
        return self.max_x() - self.min_x() + 1
    def height(self) -> int:
        return self.max_y() - self.min_y() + 1
    
    def normalize(self) -> "Tetramino":
        return self.shift(-self.min_x(), -self.min_y())

    def get_variants(self) -> list["Tetramino"]:
        variants : list["Tetramino"] = []
        for r in self.__unique_rotations:
            variants.append(deepcopy(self).rotate(r).normalize())
            if self.__mirrorable:
                variants.append(deepcopy(variants[-1]).mirror().normalize())
        return variants


    def to_svg(self) -> str:
        return "\n".join([ b.to_svg(self.__color_id) for b in self.__blocks ])

    def get_positions(self) -> list[tuple[int,int]]:
        return [ (b.x,b.y) for b in self.__blocks ]

    def get_color_id(self) -> int:
        return self.__color_id
    
    @staticmethod
    def load_tetraminos_from_json(filename:str) -> list["Tetramino"]:
        with open(filename) as f:
            return [ Tetramino(**t) for t in json.load(f) ]

if __name__ == "__main__":
    
    tetraminos = Tetramino.load_tetraminos_from_json("tetraminos/default.json")

    for id, tetramino in enumerate(tetraminos):
        tetramino.shift(5*(id%4), 5*(id//4))
    
    with open("tetraminos/default.svg", "w") as f:
        f.write("<svg width=\"1700\" height=\"800\">")
        for tetramino in tetraminos:
            f.write(tetramino.to_svg())
        f.write("</svg>")
    
    with open("tetraminos/default_variants.svg", "w") as f:
        f.write("<svg width=\"4000\" height=\"4000\">")
        for tidx, tetramino in enumerate(tetraminos):
            for vidx, variant in enumerate(tetramino.get_variants()):
                f.write(variant.shift(vidx*5,tidx*5).to_svg())
        f.write("</svg>")



