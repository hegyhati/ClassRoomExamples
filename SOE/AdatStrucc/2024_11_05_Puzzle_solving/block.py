from dataclasses import dataclass
from svg import color, SVG_BLOCK_SIZE, RECT_BLOCK_STYLE, STROKE_WIDTH

@dataclass
class Block:
    x:int = 0
    y:int = 0


    def __rotate_90_counterclockwise(self) -> None:
        self.x, self.y = -self.y, self.x

    def rotate(self, count:int = 1) -> "Block":
        for _ in range(count):
            self.__rotate_90_counterclockwise()
        return self
    
    def shift(self, dx:int=0, dy:int=0) -> "Block":
        self.x += dx
        self.y += dy
        return self
    
    def mirror_y(self) -> "Block":
        self.x *= -1
        return self
    
    def __iadd__(self, d : tuple[int,int]) -> "Block":
        return self.shift(*d)

    def to_svg(self, color_id:int = 0) -> str:
        return f'<rect width="{SVG_BLOCK_SIZE-2*STROKE_WIDTH}" height="{SVG_BLOCK_SIZE-2*STROKE_WIDTH}" x="{SVG_BLOCK_SIZE*self.x+STROKE_WIDTH}" y="{SVG_BLOCK_SIZE*self.y+STROKE_WIDTH}" fill="{color(color_id)}" stroke="{color(color_id)}" {RECT_BLOCK_STYLE} />'


if __name__ == "__main__":
    b = Block(1,2)
    b.rotate().shift(10,10)
    print(b)
    print(b.to_svg())