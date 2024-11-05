from tetramino import Tetramino
from svg import *
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
    
    def __str__(self) -> str:
        return "\n".join([
            "".join([
                "#" if self.__map[x][y] == self.FORBIDDEN else "_" if self.__map[x][y] == self.FREE else str(self.__map[x][y])
                for x in range(self.width)
            ])
            for y in range(self.height-1,-1,-1)
        ])
    
    def place_tetramino(self, tetramino:Tetramino, revert_on_failure:bool = True, min_region_size:int|None = None) -> bool:
        if tetramino.min_x() < 0 or tetramino.max_x() > self.width or tetramino.min_y() < 0 or tetramino.max_y() > self.height: return False
        for x,y in tetramino.get_positions():
            if self.__map[x][y] != self.FREE:
                if revert_on_failure:
                    for xx,yy in tetramino.get_positions():
                        if x==xx and y==yy: break
                        self.__map[x][y] = self.FREE
                return False
            self.__map[x][y] = tetramino.get_color_id()
        return True if  min_region_size is None else not self.has_small_disjoint_region(min_region_size)
        
    def to_svg(self, debug:bool=False, highlight:bool = False) -> str:
        return f""" 
            <svg width="{self.width*SVG_BLOCK_SIZE}" height="{self.height * SVG_BLOCK_SIZE}">
            <rect x="0" y="0" width="{self.width*SVG_BLOCK_SIZE}" height="{self.height * SVG_BLOCK_SIZE}" fill="{BACKGROUND_HIGHLIGHT if highlight else BACKGROUND_OK}" />
            {"".join([
                f'<rect width="{SVG_BLOCK_SIZE}" height="{SVG_BLOCK_SIZE}" x="{SVG_BLOCK_SIZE*x}" y="{SVG_BLOCK_SIZE*y}" fill="{BACKGROUND_NOK}" />'
                for x in range(self.width)
                for y in range(self.height)
                if self.__map[x][y] == self.FORBIDDEN
            ])}
            {"".join([
                f'<rect width="{SVG_BLOCK_SIZE-2*STROKE_WIDTH}" height="{SVG_BLOCK_SIZE-2*STROKE_WIDTH}" x="{SVG_BLOCK_SIZE*x+STROKE_WIDTH}" y="{SVG_BLOCK_SIZE*y+STROKE_WIDTH}" fill="{color(self.__map[x][y])}" stroke="{BACKGROUND_NOK if highlight else color(self.__map[x][y])}" {RECT_BLOCK_HIGHLIGHT_STYLE if highlight else RECT_BLOCK_STYLE}/>'
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
    
    
    def __get_free_neighbors(self, x, y) -> set[tuple[int,int]]:
        return {
            (nx, ny)
            for nx, ny in ( (x,y+1), (x,y-1), (x+1,y), (x-1,y) )
            if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height and self.__map[nx][ny] == self.FREE
        }

    def has_small_disjoint_region(self, min_region_size:int) -> bool:
        free_blocks = { (x,y) for x in range(self.width) for y in range(self.height) if self.__map[x][y] == self.FREE }
        while len(free_blocks) != 0:
            if len(free_blocks) < min_region_size: return True
            blocks_to_investigate =  { free_blocks.pop() }
            current_region = set()
            while len(blocks_to_investigate) != 0:
                current = blocks_to_investigate.pop()
                current_region.add(current)
                blocks_to_investigate.update( self.__get_free_neighbors(*current).difference(current_region))
            if len(current_region) < min_region_size: return True
            free_blocks.difference_update(current_region)
        return False


if __name__ == "__main__":
    b = Board("maps/nov5.txt")
    with open("maps/nov5_empty.svg", "w") as f:
        f.write(b.to_svg(debug=True))
    if b.place_tetramino(Tetramino(blocks=[(2,2),(3,3),(3,4),(2,4),(1,4)]), revert_on_failure=False):
        print("yeppee")
    with open("maps/nov5_nonempty.svg", "w") as f:
        f.write(b.to_svg(debug=False))
    


