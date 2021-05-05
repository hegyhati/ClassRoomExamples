from calendar_logic import Event, Calendar
import tkinter as tk
from tkinter.ttk import Combobox,Separator

_dayNames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class WeekView (tk.Frame):

    def __init__(self, master, calendar):
        super().__init__(master)
        for idx, day in enumerate(_dayNames):
            tk.Label(self, text=day, width=15).grid(row=0, column=idx+1)

        for start in range(24):
            tk.Label(
                self, text=f"{start}-{start+1}").grid(row=start+1, column=0)

        for event in calendar._events:
            self.add_event(event)

    def add_event(self, event):
        tk.Label(self, text=event.name, borderwidth=3, relief="ridge").grid(column=event.day+1, row=event.start+1, sticky="NEWS", rowspan=event.end-event.start)


class NewEventFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.nameVar = tk.StringVar(self, value="")
        self.dayVar = tk.StringVar(self, value=_dayNames[0])
        self.startVar = tk.IntVar(self, value=8)
        self.endVar = tk.IntVar(self, value=9)
        widgets = [
            tk.Label(self, text="Name:"),
            tk.Entry(self, textvariable=self.nameVar),
            tk.Label(self, text="Day:"),
            Combobox(self, textvariable=self.dayVar, values=_dayNames),
            tk.Label(self, text="Start:"),
            tk.Spinbox(self, textvariable=self.startVar, from_=0, to=23),
            tk.Label(self, text="End:"),
            tk.Spinbox(self, textvariable=self.endVar, from_=1, to=24),
            tk.Button(self, text="Add Event", command=self.new_event)
        ]
        for widget in widgets:
            widget.pack(side="top", fill="x")

    def new_event(self):
        try:
            self.master.new_event(Event(self.nameVar.get(), _dayNames.index(
                self.dayVar.get()), self.startVar.get(), self.endVar.get()))
        except Exception as e:
            self.master.display_message(f"Cannot create new event: {e}")


class CalendarManager(tk.Tk):

    def save_to_pickle(self):
        self._calendar.save_to_pickle(self._filename)

    def display_message(self,message:str):
        self.messageVar.set(message)

    def new_event(self, event):
        try:
            self._calendar.add_event(event)
            self.weekView.add_event(event)
            self.display_message("Event successfully created and added to calendar")
        except Exception as e:
            self.display_message(f"Cannot add new event: {e}")
        

    def __init__(self, filename: str = "weekly_schedule.pickle"):
        super().__init__()
        self._filename = filename
        self._calendar = Calendar()
        self._calendar.load_from_pickle(filename)
        self.messageVar=tk.StringVar(self,value="")
        self.newEvent = NewEventFrame(self)
        self.weekView = WeekView(self, self._calendar)

        tk.Button(self, text=f"SAVE Calendar to {self._filename}.", command=self.save_to_pickle).grid(row=0,column=0,columnspan=3,sticky="NEWS")    
        self.newEvent.grid(row=1, column=0,sticky="NEWS")
        Separator(self,orient="vertical").grid(row=1,column=1,sticky="ns")
        self.weekView.grid(row=1,column=2, sticky="NEWS")
        tk.Label(self,textvariable=self.messageVar,relief="sunken").grid(row=2,column=0,columnspan=3, sticky="NEWS")
