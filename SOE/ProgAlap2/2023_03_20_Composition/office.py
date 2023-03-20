from typing import List
from person import Person


class Office:
    office_number = ""
    __capacity = 0
    __occupants = []

    def __init__(self, office_number:str, capacity:int) -> None:
        self.office_number = office_number
        self.__capacity = capacity
        self.__occupants = []

    def has_free_seats(self) -> bool:
        return len(self.__occupants) < self.__capacity 

    def sit_down(self, person: Person) -> bool:
        if not self.has_free_seats(): return False
        for occupant in self.__occupants:
            if occupant._chitchat != person._chitchat:
                return False
        self.__occupants.append(person)
        return True

    def get_occupants(self) -> List[Person]:
        return self.__occupants[:] # not deep copy