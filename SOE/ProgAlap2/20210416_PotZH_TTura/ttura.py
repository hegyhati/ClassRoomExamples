import os
import os.path
import json
import matplotlib.pyplot as plt


class Acitvity:
    __mtsz_weights = {
        "hiking" : {"distance": 1.5, "100m_climb":  2},
        "cycling" : {"distance": 0.5, "100m_climb": 1}
    }

    def __init__(self, type:str, name:str, distance:float, climb:int):
        if type not in self.__mtsz_weights.keys() or name == "" or distance <= 0 or climb < 0: raise ValueError
        self.type=type
        self.name=name
        self.distance=distance
        self.climb=climb

    def is_of_type(self,type:str) -> bool:
        return type==self.type
    
    def mtsz_points(self) -> int:
        return self.distance * self.__mtsz_weights[self.type]["distance"] + self.climb//100 * self.__mtsz_weights[self.type]["100m_climb"]
    

class Calendar:

    def __init__(self,path:str):
        self.__activities=[]
        os.chdir(path)
        for filename in os.listdir():
            if ".json" in filename:
                try:
                    with open(filename) as file:
                        data = json.load(file)
                        self.__activities.append(Acitvity(data["type"],data["name"],data["distance"],data["climb"]))
                except:
                    pass
    
    def total_activity_count(self):
        return len(self.__activities)

    def total_distance(self,type:str) -> float:
        total = 0.0
        for activity in self.__activities:
            if activity.is_of_type(type):
                total += activity.distance
        return total
    
    def generate_statistics(self, filename:str):
        fig,axes=plt.subplots(2)
        types=["hiking", "cycling"]
        km =[]
        for type in types:
            km.append(self.total_distance(type))
        axes[0].bar(types,km)
        axes[0].set_title("Distance for different activity types")
        axes[0].set_ylabel("Distance (km)")
        distance=[]
        climb=[]
        for activity in self.__activities:
            if activity.is_of_type("hiking"):
                distance.append(activity.distance)
                climb.append(activity.climb)
        axes[1].scatter(distance,climb)
        axes[1].set_title("Hiking distance and climb")
        axes[1].set_xlabel("Distance (km)")
        axes[1].set_ylabel("Climb (m)")
        plt.tight_layout()
        fig.savefig(filename)


    









        