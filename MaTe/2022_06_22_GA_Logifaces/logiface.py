import random
from tkinter import Canvas
from math import atan2, degrees
from turtle import title
from typing import List
import json


SIZE = 100
LINEWIDTH = 5
OFFSETX = 10
OFFSETY = 10
COLORS = {
    1: "green",
    2: "blue",
    3: "red",
    None: "white"
}
ARCSIZE = 30

class Logiface:

    def __init__(self, heights:List[int]) -> None:
        self.heights = tuple(heights)
    
    def __str__(self):
        return "H" + str(self.heights)

class Coordinate:

    def __init__(self, row:int, column:int) -> None:
        self.row=row
        self.column=column
    
    def __str__(self) -> str:
        return f"({self.row},{self.column})"
    
    def to_tuple(self):
        return self.row, self.column

class VertexCoordinate(Coordinate):

    def __init__(self, row:int, column:int) -> None:
        super().__init__(row, column)
    
    def __str__(self) -> str:
        return f"V({self.row},{self.column})"
    
    def getX(self) -> float:
        return self.column * SIZE / 2 + OFFSETX
    
    def getY(self) -> float:
        return self.row * SIZE * 3**0.5 / 2 + OFFSETY
    
class LogifaceCoordinate(Coordinate):

    def __init__(self, row:int, column:int) -> None:
        super().__init__(row, column)
    
    def __str__(self) -> str:
        return f"T({self.row},{self.column})"

    def is_upright(self) -> bool: 
        return (self.row + self.column) % 2 == 0 
    
    def get_vertex_coordinates(self) -> List[VertexCoordinate]:
        if self.is_upright():
            return [
                VertexCoordinate(self.row, self.column),
                VertexCoordinate(self.row+1, self.column+1),
                VertexCoordinate(self.row+1, self.column-1)
            ]
        else:
            return [
                VertexCoordinate(self.row, self.column-1),
                VertexCoordinate(self.row, self.column+1),
                VertexCoordinate(self.row+1, self.column)
            ]

    def get_vertex_coordinate(self, vertex_idx:int) -> VertexCoordinate:
        return self.get_vertex_coordinates()[vertex_idx % 3]


class PlacedLogiface:

    def __init__(self, logiface:Logiface, coordinate:LogifaceCoordinate, rotation:int) -> None:
        self.logiface = logiface
        self.coordinate = coordinate
        self.rotation = rotation % 3
    
    def __str__(self) -> str:
        return f"LF({self.logiface},{self.coordinate}, {self.rotation})"

    def get_vertex_height(self, vertex_idx):
        return self.logiface.heights[ (vertex_idx - self.rotation) % 3  ]
    
    def get_vertex_coordinate(self, vertex_idx):
        return self.coordinate.get_vertex_coordinate(vertex_idx)

    def draw(self, canvas:Canvas):
        vertex_coordinates = self.coordinate.get_vertex_coordinates()
        xy_coorinates =[[vc.getX(), vc.getY()] for vc in vertex_coordinates ]
        polygon = sum(xy_coorinates, xy_coorinates[-1])
        for i in range(3):
            (px,py) = xy_coorinates[(i-1)%3]
            (x,y) = xy_coorinates[i]
            canvas.create_arc( 
                x - ARCSIZE , y - ARCSIZE, 
                x + ARCSIZE , y + ARCSIZE, 
                start = degrees(atan2(-py+y, px-x)), extent = 60, 
                fill = COLORS[self.get_vertex_height(i)]
            )
        canvas.create_polygon(polygon, outline="black", width=LINEWIDTH, fill='')
    


class Exercise:

    def __init__(self, ex_filename, set_filename) -> None:
        self._load_exercise(ex_filename)
        self._load_logiface_set(set_filename)
    
    def _load_exercise(self, filename):
        with open(filename) as f:
            coordinates = json.load(f)
        self.positions = []
        for [row,column] in coordinates:
            self.positions.append(LogifaceCoordinate(row,column))
        self.place_count = len(coordinates)
        self.height = max(pos.get_vertex_coordinate(i).getY() for pos in self.positions for i in range(3)) + OFFSETY
        self.width = max(pos.get_vertex_coordinate(i).getX() for pos in self.positions for i in range(3)) + OFFSETX
    
    def _load_logiface_set(self,filename):
        with open(filename) as f:
            logiface_heights = json.load(f)
        self.logifaces = [Logiface(heights) for heights in logiface_heights]
        self.logiface_count = len(self.logifaces)
    

    def draw(self, canvas:Canvas):
        l = Logiface([None,None,None])
        for pos in self.positions:
            PlacedLogiface(l, pos, 0).draw(canvas)


class Solution:

    def __init__(self, exercise:Exercise, selection = None, rotation = None) -> None:
        self.exercise = exercise
        self.selection = selection
        self.rotation = rotation
        if not selection:
            self.selection = random.sample(list(range(exercise.logiface_count)), k=exercise.place_count)
        if not rotation:
            self.rotation = [random.randrange(3) for _ in range(exercise.place_count)]

    def get_placed_logifaces(self):
        return [
            PlacedLogiface(
                self.exercise.logifaces[self.selection[i]],
                self.exercise.positions[i],
                self.rotation[i]
            ) for i in range(self.exercise.place_count)
        ]

    def draw(self, canvas):
        for pl in self.get_placed_logifaces():
            pl.draw(canvas)
    
    def fitness(self) -> int:
        vertex_heights = {}
        for pl in self.get_placed_logifaces():
            for vertex_idx in range(3):
                coordinate = pl.get_vertex_coordinate(vertex_idx).to_tuple()
                height =  pl.get_vertex_height(vertex_idx)
                if coordinate not in vertex_heights:
                    vertex_heights[coordinate] = [height]
                else:
                    vertex_heights[coordinate].append(height)
        error = 0
        for coordinate in vertex_heights:
            for h1 in vertex_heights[coordinate]:
                for h2 in vertex_heights[coordinate]:
                    if h1 != h2:
                        error +=1 
        return error // 2
    
    def rotate(self, position, rotation=1):
        self.rotation[position] += rotation
        self.rotation[position] %= 3








