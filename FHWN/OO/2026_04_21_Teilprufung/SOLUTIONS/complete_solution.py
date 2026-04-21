import datetime
import os
import random
import json

def get_str_value(xml_tag:str, key:str) -> str | None:
    parts = xml_tag.split(" "+key)
    return None if len(parts) == 1 or not parts[1].strip().startswith("=") else parts[1].split('"')[1]

def get_float_value(xml_tag:str, key:str) -> float | None:
    return float(value) if (value:=get_str_value(xml_tag,key)) is not None else None

def is_valid_color(colorname:str) -> bool:
    with open("colors.json") as f:
        colors = json.load(f)
    return colorname.lower().strip() in colors

class Rectangle:
    __minx: float
    __maxx: float
    __miny: float
    __maxy: float
    __color: str

    def __init__(self, topleft:tuple[float,float], bottomright:tuple[float,float], color:str):
        self.__minx = topleft[0]
        self.__miny = topleft[1]
        self.__maxx = bottomright[0]
        self.__maxy = bottomright[1]
        self.__color = color if is_valid_color(color) else "black"

    def to_svg(self) -> str:
        return f'<rect x="{self.__minx}" y="{self.__miny}" width="{self.__maxx-self.__minx}" height="{self.__maxy-self.__miny}" fill="{self.__color}" />'
    
    def covers(self, other:"Rectangle") -> bool:
        return self.__minx <= other.__minx and self.__maxx >= other.__maxx and self.__miny <= other.__miny and self.__maxy >= other.__maxy
    
    def get_random_point(self) -> tuple[float,float]:
        return random.uniform(self.__minx, self.__maxx), random.uniform(self.__miny,self.__maxy)

    def contains(self,point:tuple[float,float]) -> bool:
        return self.__minx <= point[0] <= self.__maxx and self.__miny <= point[1] <= self.__maxy

    def get_color(self) -> str:
        return self.__color 

def write_to_svg(filename:str, width:float, height:float, rectangles:list[Rectangle]) -> None:
    with open(filename, "w") as f:
        f.write(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
        for rectangle in rectangles:
            f.write(rectangle.to_svg()+'\n')
        f.write('</svg>\n')

def load_from_svg(filename:str) -> list[Rectangle]:
    rectangles = []
    with open(filename) as f:
        for line in f:
            if "<rect" in line:
                x = get_float_value(line,"x")
                y = get_float_value(line,"y")
                w = get_float_value(line,"width")
                h = get_float_value(line,"height")
                c = get_str_value(line,"fill")
                if x is not None and y is not None and w is not None and h is not None and c is not None:
                    rectangles.append(Rectangle((x,y),(x+w,y+h),c))
    return rectangles

def fetch_width_height(filename:str) -> tuple[float,float]: 
    with open(filename) as f:
        for line in f:
            if "<svg " in line:
                return get_float_value(line,"width"), get_float_value(line,"height")

def filter_by_individual_cover(filename:str, suffix:str="_fbic") -> None:
    w,h = fetch_width_height(filename)
    rectangles = load_from_svg(filename)
    filtered:list[Rectangle] = []
    for idx1 in range(len(rectangles)):
        for idx2 in range(idx1+1, len(rectangles)):
            if rectangles[idx2].covers(rectangles[idx1]):
                break
        else:
            filtered.append(rectangles[idx1])
    name,ext = os.path.splitext(filename)
    write_to_svg(name+suffix+ext,w,h,filtered)

TRIES = 10000
def probabilistic_filter(filename:str, suffix:str="_pf") -> None:
    w,h = fetch_width_height(filename)
    rectangles = load_from_svg(filename)
    filtered:list[Rectangle] = []
    for idx1 in range(len(rectangles)):
        for _ in range(TRIES):
            point = rectangles[idx1].get_random_point()
            for idx2 in range(idx1+1, len(rectangles)):
                if rectangles[idx2].contains(point):
                    break
            else:
                filtered.append(rectangles[idx1])
                break
    name,ext = os.path.splitext(filename)
    write_to_svg(name+suffix+ext,w,h,filtered)




# Make a random one and test the filters

def generate_random_rectangle(size:int = 500, scale:int=10) -> Rectangle:
    SSIZE = size/scale
    with open("colors.json") as f:
        colors = json.load(f)
    x = int(random.uniform(0,SSIZE*3/4))
    y = int(random.uniform(0,SSIZE*3/4))
    side = int(random.uniform(min(SSIZE/8,SSIZE-x), min(SSIZE/2,SSIZE-x, SSIZE-y)))
    x*=scale
    y*=scale
    side*=scale
    return Rectangle(
        topleft=(x,y),
        bottomright=(x+side, y+side),
        color = random.choice(colors)
    )
    
if __name__ == "__main__":
    FILENAME = f"{datetime.datetime.now()}.svg"
    rectangles:list[Rectangle] = [generate_random_rectangle() for _ in range(1000)]
    write_to_svg(FILENAME, rectangles)
    filter_by_individual_cover(FILENAME)
    probabilistic_filter(FILENAME)