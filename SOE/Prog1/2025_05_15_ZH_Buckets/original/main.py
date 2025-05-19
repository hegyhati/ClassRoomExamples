import datetime
import json
import os
import random

from matplotlib import pyplot as plt


class Bucket:
    def __init__(self, capacity:float) -> None:
        if capacity <= 0: raise ValueError("Capacity must be positive.")
        self.__capacity = capacity
        self._level = 0
    
    def get_level(self) -> float:
        return self._level
    
    def get_capacity(self) -> float:
        return self.__capacity

    def get_remaining_capacity(self) -> float:
        return self.__capacity - self._level
    
    def __pour_into(self, other:"Bucket", amount:float):
            other._level += amount
            self._level -= amount
    
    def empty(self) -> None:
        self._level = 0
    
    def fill(self) -> None:
        self._level = self.__capacity
        

    def pour_into(self, other:"Bucket"):
        self.__pour_into(other, min(other.get_remaining_capacity(), self._level))

class BucketSystem:
    def __init__(self) -> None:
        self.__buckets:dict[str,Bucket] = {}
    
    def add_bucket(self, name:str, capacity:float) -> None:
        if name in self.__buckets: raise ValueError(f"Bucket with name {name} already exists.")
        self.__buckets[name] = Bucket(capacity)

    def empty_buckets(self, buckets:list[str]) -> None:
        for name in buckets:
            if name in self.__buckets:
                self.__buckets[name].empty()

    def fill_buckets(self, buckets:list[str]) -> None:
        for name in buckets:
            if name in self.__buckets:
                self.__buckets[name].fill()
    
    def pour(self, source:str, sink:str) -> None:
        if source not in self.__buckets: raise ValueError(f"{source} bucket does not exist.")
        if sink not in self.__buckets: raise ValueError(f"{sink} bucket does not exist.")
        self.__buckets[source].pour_into(self.__buckets[sink])
    
    def get_levels(self) -> list[tuple[str,float,float]]:
        return [
            (name, bucket.get_level(), bucket.get_capacity())
            for name, bucket in self.__buckets.items()
        ]
    
    def has_volume(self, volume:float) -> bool:
        for name, bucket in self.__buckets.items():
            if bucket.get_level() == volume: 
                return True
        return False

CHALLENGEDIR = "challenges"
GAMEDIR = "games"


class Game:
    def __init__(self, capacities:dict[str,float], goal:float, steplimit:int) -> None:
        self.__goal = goal
        self.__maxsteps = steplimit
        self.__steps_remaining = steplimit
        self.__buckets = BucketSystem()
        for name, capacity in capacities.items():
            self.__buckets.add_bucket(name,capacity)
        
    def __str__(self):
        return "\n".join([
            f"Goal: {self.__goal}",
            f"Steps remaining: {self.__steps_remaining}",
            "Buckets:",
            *[f" - {name}: {level}/{capacity}" for (name,level,capacity) in self.__buckets.get_levels()]
        ])
    
    def __export_state(self):
        fig,ax = plt.subplots()
        steps = self.__maxsteps - self.__steps_remaining
        plt.suptitle(f"Goal: {self.__goal}, steps: {steps}/{self.__maxsteps}")
        names, levels, capacities = zip(*self.__buckets.get_levels())
        ax.bar(names, capacities, color='lightblue', edgecolor='black')
        ax.bar(names, levels, color='blue', edgecolor='black')
        fig.savefig(os.path.join(GAMEDIR,self.__game_start,f"{steps:03}.jpg"))


    def run(self) -> bool:
        self.__game_start = datetime.datetime.now().isoformat().replace(":","-")
        os.makedirs(os.path.join(GAMEDIR,self.__game_start))
        self.__export_state()
        while self.__steps_remaining > 0:
            print(self)
            command = input("\n".join([
                "What do you want to do?",
                " - ABORT",
                " - FILL bucket1 bucket2 ...",
                " - EMPTY bucket1 bucket2 ...",
                " - POUR source_bucket sink_bucket",
                "Your command: "
            ]))
            try:
                match command.strip().split(" "):
                    case ["ABORT"]: return False
                    case ["FILL", *buckets]: self.__buckets.fill_buckets(buckets)
                    case ["EMPTY", *buckets]: self.__buckets.empty_buckets(buckets)
                    case ["POUR", source, sink]: self.__buckets.pour(source, sink)
                    case _: raise ValueError("Invalid command.")            
                self.__steps_remaining -= 1
                self.__export_state()
            except ValueError as e:
                print(f"Error: {e}")
            if self.__buckets.has_volume(self.__goal):
                print("Woooohoooo!!!")
                return True
        print("You ran out of steps, game over.")
        return False
    

BUCKETNAMEFILE = "bucketnames.json"
if __name__ == "__main__":
    print("Which challenge do you want to play?")
    for file in os.listdir(CHALLENGEDIR):
        if os.path.isfile(os.path.join(CHALLENGEDIR,file)):
            name, ext = os.path.splitext(file)
            if ext == ".json":
                print(f" - {name}")    
    challenge = os.path.join(CHALLENGEDIR, input() + ".json")
    if not os.path.isfile(challenge): 
        print("No such challenge")
        exit()
    with open(challenge) as f:
        data = json.load(f)
    with open(BUCKETNAMEFILE) as f:
        names = random.sample(json.load(f),k=len(data["capacities"]))
    Game(dict(zip(names,data["capacities"])),data["goal"],data["steplimit"]).run()
    
    

    

    


        

    


