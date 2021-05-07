import json
import tkinter as tk
from tkinter.ttk import Separator


class Bike:

    def __init__(self, filename: str):
        with open(filename, "rt") as file:
            data = json.load(file)
        self.front = data["chainring"]
        self.rear = data["cassette"]
        self.circumference = data["wheel_diameter"] * \
            3.14 / 1000 / 1000  # in km
        self.current = 0

    def get_current_gear(self):
        return self.current+1

    def get_current_teeths(self):
        return self.rear[self.current]

    def shift_up(self):
        if self.current + 1 < len(self.rear):
            self.current += 1

    def shift_down(self):
        if self.current > 0:
            self.current -= 1


class BikeUI(tk.Tk):

    def __init__(self, filename):
        super().__init__()
        self.bike = Bike(filename)
        self.cadence = tk.DoubleVar(value=90)
        self.speed = tk.DoubleVar()
        self.gear = tk.IntVar(value=self.bike.get_current_gear())
        widgets = [
            tk.Label(self, text="Cadence in rpm:"),
            tk.Entry(self, textvariable=self.cadence),
            Separator(self, orient="horizontal"),
            tk.Label(self, text="GEAR"),
            tk.Button(self, text="SHIFT UP", command=self.__shift_up),
            tk.Label(self, textvariable=self.gear),
            tk.Button(self, text="SHIFT DOWN", command=self.__shift_down),
            Separator(self, orient="horizontal"),
            tk.Label(self, text="Speed in km/h:"),
            tk.Label(self, textvariable=self.speed)
        ]
        for widget in widgets:
            widget.pack(side="top", fill="x")
        self.__update()

    def __shift_up(self):
        self.bike.shift_up()
        self.__update()

    def __shift_down(self):
        self.bike.shift_down()
        self.__update()

    def __update(self):
        self.gear.set(self.bike.get_current_gear())
        pedal_rounds = 60.0 * self.cadence.get()
        chains_passed = pedal_rounds * self.bike.front
        wheel_rounds = chains_passed / self.bike.get_current_teeths()
        distance = wheel_rounds * self.bike.circumference
        self.speed.set(distance)


BikeUI("bike.json").mainloop()
