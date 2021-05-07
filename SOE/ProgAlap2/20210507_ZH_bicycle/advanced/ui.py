import tkinter as tk
from functools import partial


class BikeCalculator(tk.Tk):

  def __init__(self, bike):
    super().__init__()
    self.__bike = bike
    self.__cadenceVar = tk.DoubleVar(value=90.0)
    self.__cadenceVar.trace_add("write", self.__update_speed)
    self.__speedVar = tk.DoubleVar()
    self.__front_gear=tk.IntVar(value=bike.get_front_gear())
    self.__rear_gear=tk.IntVar(value=bike.get_rear_gear())
    self.__update_speed()
    self.title("Speed calculator")
    self.resizable(False,False)

    widget_columns = [[
        tk.Label(self, text="Cadence"),
        tk.Entry(self, textvariable=self.__cadenceVar),
        tk.Label(self, text="rpm")
      ], [
        tk.Label(self,text="Chainring"),
        tk.Button(self,text="▲", command = partial(self.__update_gear, self.__bike.shift_front_up)),
        tk.Label(self,textvariable=self.__front_gear),
        tk.Button(self,text="▼", command = partial(self.__update_gear, self.__bike.shift_front_down))
      ], [
        tk.Label(self,text="Cassette"),
        tk.Button(self,text="▲", command = partial(self.__update_gear, self.__bike.shift_rear_up)),
        tk.Label(self,textvariable=self.__rear_gear),
        tk.Button(self,text="▼", command = partial(self.__update_gear, self.__bike.shift_rear_down))
      ], [
        tk.Label(self, text="Speed"),
        tk.Entry(self, textvariable=self.__speedVar),
        tk.Label(self, text="km/h")
      ]]
    for (c,widget_column) in enumerate(widget_columns):
      for (r,widget) in enumerate(widget_column):
        widget.grid(row=r, column=c, sticky="NEWS")

  def __update_gear(self, gear_change):
    gear_change()
    self.__front_gear.set(self.__bike.get_front_gear())
    self.__rear_gear.set(self.__bike.get_rear_gear())
    self.__update_speed()

  def __update_speed(self, *_):
    self.__speedVar.set(self.__bike.get_speed(self.__cadenceVar.get()))


