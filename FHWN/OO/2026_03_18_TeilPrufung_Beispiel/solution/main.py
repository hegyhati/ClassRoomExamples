import json
import os

def parse_latitude(trkpt_str:str) -> float:
    return float(trkpt_str.split("lat")[1].split('"')[1])

def parse_longitude(trkpt_str:str) -> float:
    return float(trkpt_str.split("lon")[1].split('"')[1])

def distance(pos1:tuple[float,float], pos2:tuple[float,float]) -> float:
    dlat = 111000 * (pos1[0]-pos2[0])
    dlon = 75000 * (pos1[1]-pos2[1])
    return (dlat ** 2 + dlon ** 2) ** 0.5

def is_close(pos1:tuple[float,float], pos2:tuple[float,float], treshold_m:float = 50) -> bool:
    return distance(pos1,pos2) <= treshold_m 

class POI_Manager:
    __file : str

    def __init__(self, filename:str):
        self.__file = filename

    def __get_data(self) -> list[dict]:
        with open(self.__file, encoding="utf-8") as f:
            return json.load(f)
    
    def __persist_data(self, data:list[dict]) -> None:
        with open(self.__file, "w", encoding="utf-8") as f:
            return json.dump(data,f, ensure_ascii=False, indent=4)
    
    def __get_poi_by_name(self, name:str) -> dict|None:
        for poi in self.__get_data():
            if poi["name"] == name:
                return poi
        return None
    
    def get_poi_count(self) -> int:
        return len(self.__get_data())
    
    def get_pois(self) -> set[str]:
        return {poi["name"] for poi in self.__get_data()}
    
    def get_pos(self, name:str) -> tuple[float,float]|None:
        poi = self.__get_poi_by_name(name)
        return (poi["pos"]["lat"], poi["pos"]["lon"]) if poi is not None else None

    def add_new_poi(self, name:str, pos:tuple[float,float]) -> None:
        self.__persist_data(self.__get_data() + [{
            "name" : name,
            "pos" : {
                "lat" : pos[0],
                "lon" : pos[1]
            }
        }])
    
    def get_close_pois(self, pos:tuple[float]) -> set[str]:
        return { poi["name"]
            for poi in self.__get_data()
            if is_close(pos, (poi["pos"]["lat"],poi["pos"]["lon"]))
        }

    def get_visits(self, name:str) -> int|None:
        data = self.__get_data()
        for poi in data:
            if poi["name"] == name:
                if "visits" in poi:
                    return poi["visits"]
                else:
                    poi["visits"] = 0
                    self.__persist_data(data)
                    return 0
        return None    

    def _add_visit(self, name:str) -> None:
        data = self.__get_data()
        for poi in data:
            if poi["name"] == name:
                if "visits" not in poi:
                    poi["visits"] = 0
                poi["visits"] +=1
                self.__persist_data(data)
                return

    def top_visits(self, count:int = 5)->list[str]:
        data = self.__get_data()
        data.sort(key = lambda poi: poi["visits"] if "visits" in poi else 0, reverse=True)
        return [poi["name"] for poi in data[:count]]
    
    def process_gpx(self, filepath:str) -> set[str]:
        visited = set()
        with open(filepath) as f:
            for line in f:
                if "<trkpt" in line:
                    lat = parse_latitude(line)
                    lon = parse_longitude(line)
                    pois = self.get_close_pois((lat,lon))
                    for poi in pois:
                        if poi not in visited:
                            visited.add(poi)
                            self._add_visit(poi)
        return visited

if __name__ == "__main__":

    manager = POI_Manager("../poi.json")
    while True:
        selection = input("""
            What do you want to do?
            1) Search for a POI
            2) Add new POI
            3) TOP 5 most popular POIs
            4) Add visits from GPX files in a directory
            5) Exit
            """)
        match selection.strip():
            case "1":
                substr = input("Search for: ")
                print("Matching POIs:")
                for poi in manager.get_pois():
                    if substr.lower() in poi.lower():
                        print(f" - {poi} {manager.get_pos(poi)}")
                print()
            case "2":
                name = input("Name of the POI: ")
                pos = input("lat,lon: ")
                pos = tuple(float(p) for p in pos.split(","))
                close_pois = manager.get_close_pois(pos)
                if len(close_pois) > 0:
                    answer = input("These POIs are close: " + ",".join(close_pois) + f"\nAre you sure, you want to add {name} {pos}? Yes/No")
                    if "yes" not in answer.lower():
                        continue
                manager.add_new_poi(name,pos)
            case "3":
                top = manager.top_visits()
                for i,name in enumerate(top):
                    print(f"{i+1}. {name} {manager.get_pos(name)} - {manager.get_visits(name)} visit(s)")
            case "4":
                dirpath = input("Where should I look for GPX files? ")
                for file in os.listdir(dirpath):
                    if os.path.splitext(file)[1] == ".gpx":
                        print(f" - Checking {file}... ", end="")
                        pois = manager.process_gpx(os.path.join(dirpath,file))
                        print(" visited: " + ", ".join(pois))
            case "5":
                print("Bye-bye")
                exit(0)
            case _: 
                print("Wrong command, try again.")





