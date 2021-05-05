import json
import pickle

class Event:
    def __init__(self, name: str, day: int, start: int, end: int) -> None:
        self.name = name
        self.day = day
        self.start = start
        self.end = end
        self._validate()

    def _validate(self) -> None:
        if self.name in ["", None]:
            raise Exception("Invalid name for event, should not be empty.")
        if self.day < 0 or self.day > 6:
            raise Exception("Invalid day, should be between 0 and 6.")
        if self.end <= self.start:
            raise Exception("End must be later than beginning.")
        return True

    def overlaps_with(self, otherEvent) -> bool:
        return self.day == otherEvent.day and self.end > otherEvent.start and otherEvent.end > self.start
    
    def export_to_json(self) -> str:
        return f'{{"name" : "{self.name}", "day" : {self.day}, "start": {self.start}, "end" : {self.end} }}'


class Calendar:
    def __init__(self) -> None:
        self._events = set()
            
    def add_event(self, event):
        for fixed_event in self._events:
            if fixed_event.overlaps_with(event):
                raise Exception("Overlaps with other event.")
        self._events.add(event)
    
    def save_to_json(self,filename:str="weekly_schedule.json"):
        json_export="["
        first=True
        for event in self._events:
            if not first: 
                json_export += ","
            json_export += "\n\t" + event.export_to_json()
            first = False
        json_export+="\n]\n"
        with open(filename,"wt") as file:
            file.write(json_export)

    def load_from_json(self,filename:str="weekly_schedule.json"):
        with open(filename,"rt") as file:
            data = json.load(file)
            for event_dict in data:
                self.add_event(Event(**event_dict))
  
    def save_to_pickle(self, filename:str="weekly_schedule.pickle"):
        with open(filename,"bw") as file:
            file.write(pickle.dumps(self._events))
    
    def load_from_pickle(self,filename:str="weekly_schedule.pickle"):
        with open(filename,"br") as file:
            self._events=pickle.load(file)
        
    
    

if __name__=="__main__":
   
    myWeek=Calendar()
    myWeek.load_from_pickle()
    name=input("Name: ")
    day=int(input("Day: "))
    start=int(input("Start: "))
    end=int(input("End: "))
    try:
        myWeek.add_event(Event(name,day,start,end))
    except Exception as e:
        print(f"Not ok: {e}")
    myWeek.save_to_pickle()
    myWeek.save_to_json()
