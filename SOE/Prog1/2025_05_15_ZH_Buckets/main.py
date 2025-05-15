import datetime
import json
import os
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
    
    def empty(self) -> None:
        self._level = 0
    
    def fill(self) -> None:
        self._level = self.__capacity
    
    def __pour_into(self, other:"Bucket", amount:float):
            other._level += amount
            self._level -= amount        

    def pour_into(self, other:"Bucket"):
        self.__pour_into(other, min(other.get_remaining_capacity(), self._level))

class BucketSystem:
    def __init__(self) -> None:
        self.__buckets:list[Bucket] = []
    
    def add_bucket(self, capacity:float) -> None:
        self.__buckets.append(Bucket(capacity))
    
    def bucket_count(self) -> int:
        return len(self.__buckets)

    def __valid_bucket_idx(self, idx:int) -> bool:
        return idx >= 0 and idx < len(self.__buckets)

    def empty_buckets(self, buckets:list[int]) -> None:
        if not all(self.__valid_bucket_idx(idx) for idx in buckets): raise ValueError("Some indices are bad.")
        for idx in buckets:
            self.__buckets[idx].empty()

    def fill_buckets(self, buckets:list[int]) -> None:
        if not all(self.__valid_bucket_idx(idx) for idx in buckets): raise ValueError("Some indices are bad.")
        for idx in buckets:
            print(idx)
            self.__buckets[idx].fill()
    
    def pour(self, source:int, sink:int) -> None:
        if source == sink: raise ValueError("Source and Sink cannot be the same.")
        if not self.__valid_bucket_idx(source): raise ValueError("Source is not a valid bucket.")
        if not self.__valid_bucket_idx(sink): raise ValueError("Sink is not a valid bucket.")
        self.__buckets[source].pour_into(self.__buckets[sink])
    
    def get_levels(self) -> list[tuple[float,float]]:
        return [(bucket.get_level(), bucket.get_capacity()) for bucket in self.__buckets]
    
    def has_volume(self, volume:float) -> bool:
        return any(bucket.get_level() == volume for bucket in self.__buckets)

CHALLENGEDIR = "challenges"
GAMEDIR = "games"

class Game:
    def __init__(self, capacities:list[float], goal:float, steplimit:int) -> None:
        self.__goal = goal
        self.__maxsteps = steplimit
        self.__step_counter = 0
        self.__buckets = BucketSystem()
        for capacity in capacities:
            self.__buckets.add_bucket(capacity)
        
    def __str__(self):
        return "\n".join([
            f"Goal: {self.__goal}",
            f"Steps remaining: {self.__maxsteps - self.__step_counter}",
            "Buckets:",
            *[f" - {idx}: {level}/{capacity}" for idx,(level,capacity) in enumerate(self.__buckets.get_levels())]
        ])
    
    def __export_state(self):
        fig,ax = plt.subplots()
        plt.suptitle(f"Goal: {self.__goal}, steps: {self.__step_counter}/{self.__maxsteps}")
        levels, capacities = zip(*self.__buckets.get_levels())
        x = list(map(str,range(self.__buckets.bucket_count())))
        ax.bar(x, capacities, color='lightblue', edgecolor='black')
        ax.bar(x, levels, color='blue', edgecolor='black')
        fig.savefig(os.path.join(GAMEDIR,self.__game_start,f"{self.__step_counter:03}.jpg"))


    def run(self) -> bool:
        self.__game_start = datetime.datetime.now().isoformat()
        os.makedirs(os.path.join(GAMEDIR,self.__game_start))
        self.__export_state()
        while self.__step_counter < self.__maxsteps:
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
                    case ["FILL", *buckets]: self.__buckets.fill_buckets(list(map(int,buckets)))
                    case ["EMPTY", *buckets]: self.__buckets.empty_buckets(list(map(int,buckets)))
                    case ["POUR", source, sink]: self.__buckets.pour(int(source), int(sink))
                    case _: raise ValueError("Invalid command.")            
                self.__step_counter += 1
                self.__export_state()
            except ValueError as e:
                print(f"Error: {e}")
            if self.__buckets.has_volume(self.__goal):
                print("Woooohoooo!!!")
                return True
        print("You ran out of steps, game over.")
        print(self)
        return False
    

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
    Game(data["capacities"],data["goal"],data["steplimit"]).run()
    
    

    

    


        

    


