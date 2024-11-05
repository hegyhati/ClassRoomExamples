from tetramino import Tetramino
from svg import color, BACKGROUND_OK, BACKGROUND_NOK, SVG_BLOCK_SIZE, RECT_BLOCK_STYLE, STROKE_WIDTH
import json

class Board:

    FREE = -1
    FORBIDDEN = -2

    __char_to_value = {
        "_" : FREE,
        "#" : FORBIDDEN
    }

    def __init__(self, filename:str) -> None:
        with open(filename) as f:
            tmp = [ [ self.__char_to_value[c] for c in line.strip() ] for line in f ]
        self.height = len(tmp)
        self.width = len(tmp[0])
        self.__map = [
            [ tmp[y][x] for y in range(self.height)]
            for x in range(self.width)
        ]
    
    def place_tetramino(self, tetramino:Tetramino, revert_on_failure:bool = True) -> bool:
        if tetramino.min_x() < 0 or tetramino.max_x() > self.width or tetramino.min_y() < 0 or tetramino.max_y() > self.height: return False
        for x,y in tetramino.get_positions():
            if self.__map[x][y] != self.FREE:
                if revert_on_failure:
                    for xx,yy in tetramino.get_positions():
                        if x==xx and y==yy: break
                        self.__map[x][y] = self.FREE
                return False
            self.__map[x][y] = tetramino.get_color_id()
        return True
        
    def to_svg(self, debug:bool=False) -> str:
        return f""" 
            <svg width="{self.width*SVG_BLOCK_SIZE}" height="{self.height * SVG_BLOCK_SIZE}">
            <rect x="0" y="0" width="{self.width*SVG_BLOCK_SIZE}" height="{self.height * SVG_BLOCK_SIZE}" fill="{BACKGROUND_OK}" />
            {"".join([
                f'<rect width="{SVG_BLOCK_SIZE}" height="{SVG_BLOCK_SIZE}" x="{SVG_BLOCK_SIZE*x}" y="{SVG_BLOCK_SIZE*y}" fill="{BACKGROUND_NOK}" />'
                for x in range(self.width)
                for y in range(self.height)
                if self.__map[x][y] == self.FORBIDDEN
            ])}
            {"".join([
                f'<rect width="{SVG_BLOCK_SIZE-2*STROKE_WIDTH}" height="{SVG_BLOCK_SIZE-2*STROKE_WIDTH}" x="{SVG_BLOCK_SIZE*x+STROKE_WIDTH}" y="{SVG_BLOCK_SIZE*y+STROKE_WIDTH}" fill="{color(self.__map[x][y])}" stroke="{color(self.__map[x][y])}" {RECT_BLOCK_STYLE}/>'
                for x in range(self.width)
                for y in range(self.height)
                if self.__map[x][y] not in  (self.FORBIDDEN, self.FREE)
            ])}
            {"".join([
                f'<text  x="{SVG_BLOCK_SIZE*x+5}" y="{SVG_BLOCK_SIZE*y+15}">{x,y}</text>'
                for x in range(self.width)
                for y in range(self.height)
            ]) if debug else ""}
            {"".join([
                f'<line x1="{x*SVG_BLOCK_SIZE}" y1="0" x2="{x*SVG_BLOCK_SIZE}" y2="{self.height*SVG_BLOCK_SIZE}" stroke = "black" stroke-width = "2"/>'
                for x in range(1,self.width)
            ]) if debug else ""}
            {"".join([
                f'<line x1="{0}" y1="{y*SVG_BLOCK_SIZE}" x2="{self.width*SVG_BLOCK_SIZE}" y2="{y*SVG_BLOCK_SIZE}" stroke = "black" stroke-width = "2"/>'
                for y in range(1,self.height)
            ]) if debug else ""}
            </svg>
            """

if __name__ == "__main__":
    b = Board("maps/nov5.txt")
    with open("maps/nov5_empty.svg", "w") as f:
        f.write(b.to_svg(debug=True))
    if b.place_tetramino(Tetramino(blocks=[(2,2),(3,3),(3,4),(2,4),(1,4)]), revert_on_failure=False):
        print("yeppee")
    with open("maps/nov5_nonempty.svg", "w") as f:
        f.write(b.to_svg(debug=False))
    


