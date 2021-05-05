from calendar_logic import Event, Calendar
import tkinter as tk
from tkinter.ttk import Combobox


class WeekView (tk.Frame):
    __dayNames = ["Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, parent, calendar):
        super().__init__(parent)
        for idx, day in enumerate(self.__dayNames):
            tk.Label(self, text=day).grid(row=0, column=idx+1)

        for start in range(24):
            tk.Label(
                self, text=f"{start}-{start+1}").grid(row=start+1, column=0)

        self.__calendar = calendar
        for event in calendar._events:
            self.new_event(event)

    def new_event(self, event):
        tk.Label(self, text=event.name, borderwidth=3, relief="ridge").grid(
            column=event.day+1, row=event.start+1, sticky="NSEW", rowspan=event.end-event.start)


class NewEventFrame(tk.Frame):
    __dayNames = ["Monday", "Tuesday", "Wednesday",
                  "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, parent):
        super().__init__(parent)
        widgets = []
        widgets.append(tk.Label(self, text="Name:"))
        self.nameVar = tk.StringVar(self, value="")
        widgets.append(tk.Entry(self, textvariable=self.nameVar))
        widgets.append(tk.Label(self, text="Day:"))
        self.dayVar = tk.StringVar(self, value=self.__dayNames[0])
        widgets.append(
            Combobox(self, textvariable=self.dayVar, values=self.__dayNames))
        widgets.append(tk.Label(self, text="Start:"))
        self.startVar = tk.IntVar(self, value=8)
        widgets.append(tk.Spinbox(
            self, textvariable=self.startVar, from_=0, to=23))
        widgets.append(tk.Label(self, text="End:"))
        self.endVar = tk.IntVar(self, value=9)
        widgets.append(tk.Spinbox(
            self, textvariable=self.endVar, from_=1, to=24))
        widgets.append(
            tk.Button(self, text="Add Event", command=self.new_event))
        self.messageVar = tk.StringVar(self, value="")
        widgets.append(tk.Label(self, textvariable=self.messageVar))

        for widget in widgets:
            widget.pack(side="top", fill="x")

    def new_event(self):
        try:
            newEvent = Event(self.nameVar.get(), self.__dayNames.index(
                self.dayVar.get()), self.startVar.get(), self.endVar.get())
            self.messageVar.set("Event successfully created.")
            self.master.new_event(newEvent)            
        except Exception as e:
            self.messageVar.set(f"Cannot create new event: {e}")


class CalendarManager(tk.Tk):

    def save_to_pickle(self):
        self._calendar.save_to_pickle(self._filename)

    def new_event(self, event):
        try:
            self._calendar.add_event(event)
            self.weekView.new_event(event)
        except Exception as e:
            self.newEvent.messageVar.set(f"Cannot add new event: {e}")
        

    def __init__(self, filename: str = "weekly_schedule.pickle"):
        super().__init__()
        self._filename = filename
        self._calendar = Calendar()
        self._calendar.load_from_pickle(filename)

        tk.Button(self, text=f"SAVE Calendar to {self._filename}.", command=self.save_to_pickle).pack(
            side="top", fill="x")

        self.newEvent = NewEventFrame(self)
        self.newEvent.pack(side="left")

        self.weekView = WeekView(self, self._calendar)
        self.weekView.pack(side="left")
