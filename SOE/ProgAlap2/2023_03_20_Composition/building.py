from office import Office
from person import Person


class Building:
    def __init__(self, name:str) -> None:
        self._name = name
        self._offices = []

    def new_office(self, capacity: int) -> None:
        self._offices.append(Office(
            self._name + "-" + str(len(self._offices)),
            capacity
        ))

    def sit_down(self,person: Person) -> None:
        for office in self._offices:
            if office.sit_down(person):
                return

    def print_offices(self) -> None:
        for office in self._offices:
            print(f"Office {office.office_number}:")
            for occupant in office.get_occupants():
                print(f" - {occupant}")