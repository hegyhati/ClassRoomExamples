from tkinter import Tk, Frame, Label, Button, Entry, messagebox, DoubleVar, TclError
from tkinter import BOTH, LEFT, SOLID, TOP, W, E, BOTTOM
from tkinter.ttk import Combobox
from functools import partial

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from database import Route, POI, Visit, Color, Shape


from PIL import Image, ImageTk
import os


class MainWindow(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Soproni turistajelzes DB")
        self.minsize(500,100)
        SelectorFrame(self).pack(fill=BOTH)
    
    def replace_frame(self, to_destroy, new_cls, **kargs):
        to_destroy.destroy()
        new_frame = new_cls(self, **kargs)
        if hasattr(new_cls, "_back_frame"):
            Button(new_frame, text="Back", background="gray", command=partial(self.replace_frame, new_frame, new_cls._back_frame)).pack(fill=BOTH, side=BOTTOM)
        new_frame.pack(fill=BOTH)

class TitleLabel(Label):
    def __init__(self, master, text) -> None:
        super().__init__(master, text=text, font=("Arial", 20), padx=10, pady=10, border=1, relief=SOLID, background="gray")
        self.pack(fill=BOTH, side=TOP)

class TouristSignLabel(Label):
    def __init__(self, master, route:Route) -> None:
        super().__init__(master)
        filename = os.path.join("signs", f"{route.color}{route.shape}.jpg")
        if os.path.exists(filename):
            self.image = ImageTk.PhotoImage(Image.open(filename))
        else:
            self.image = ImageTk.PhotoImage(Image.open(os.path.join("signs", "missing.jpg")))
        self.config(image=self.image)

class SelectorFrame(Frame):    
    def __init__(self, master) -> None:
        super().__init__(master)
        TitleLabel(self, text="Select an option")
        Button(self, text="Routes", command=partial(master.replace_frame, self, RouteListFrame)).pack(fill=BOTH)
        Button(self, text="POIs",command=partial(master.replace_frame, self, POIListFrame)).pack(fill=BOTH)
        Button(self, text="New Route", command=partial(master.replace_frame, self, NewRouteFrame)).pack(fill=BOTH)
        Button(self, text="Exit", command=self.quit).pack(fill=BOTH)

class RouteListFrame(Frame):
    _back_frame = SelectorFrame
    class RouteOverviewFrame(Frame):
        def __init__(self, master, route:Route) -> None:
            super().__init__(master, borderwidth=1)
            TouristSignLabel(self,route).pack(side=LEFT)
            Label(self, text=f"{route.distance} km").pack(side=LEFT)
            Button(self, text = "Show details", command=partial(master.master.replace_frame, master, RouteDetailsFrame, route_id = route.id)).pack(side=LEFT)


    def __init__(self, master) -> None:
        super().__init__(master)
        TitleLabel(self, "Routes")
        with Session(engine) as session:
            for route in session.query(Route).all():
                RouteListFrame.RouteOverviewFrame(self, route).pack(fill=BOTH, padx=10, pady=10)

class RouteDetailsFrame(Frame):
    _back_frame = RouteListFrame
    def __init__(self, master, route_id:int) -> None:
        super().__init__(master)
        with Session(engine) as session:
            route = session.execute(select(Route).where(Route.id == route_id)).scalars().first()
            TouristSignLabel(self,route).pack(fill=BOTH)
            poi_frame = Frame(self)
            pois = [ poi for poi in route.pois]
            pois.sort(key=lambda poi: poi.position)
            count = 0
            for count, poi in enumerate(pois):
                Label(poi_frame, text=f"{poi.position} km - ").grid(row=count, column=0, sticky=E)
                Label(poi_frame, text=f"{poi.poi.name}").grid(row=count, column=1, sticky=W)
            Label(poi_frame, text=f"{route.distance} km - ").grid(row=count+1, column=0, sticky=E)
            Label(poi_frame, text="Utvonal vege").grid(row=count+1, column=1, sticky=W)
            poi_frame.pack(fill=BOTH)

class POIListFrame(Frame):
    _back_frame = SelectorFrame
    def __init__(self, master) -> None:
        super().__init__(master)
        TitleLabel(self, "POIs")
        with Session(engine) as session:
            for poi in session.query(POI).all():
                Label(self, text=f"{poi.name}\n{poi.description}", anchor=W, justify=LEFT).pack(fill=BOTH, padx=10, pady=10)
            

class NewRouteFrame(Frame):
    _back_frame = SelectorFrame

    def __init__(self, master) -> None:
        super().__init__(master)
        self.colors = {
            "Kek": Color.blue,
            "Piros": Color.red,
            "Sarga": Color.yellow,
            "Zold": Color.green,
            "Egyeb": Color.other
        }
        self.shapes = {
            "Sav" : Shape.line,
            "Kereszt" : Shape.cross,
            "Haromszog" : Shape.triangle,
            "Kor" : Shape.circle,
            "Negyzet" : Shape.square,
            "Rom" : Shape.ruin,
            "Barlang" : Shape.cave,
            "Egyeb" : Shape.other
        }

        TitleLabel(self, "New Route")
        Label(self, text="Color").pack(fill=BOTH)
        self.color_selector = Combobox(self, values=list(self.colors.keys()))
        self.color_selector.pack(fill=BOTH)
        Label(self, text="Shape").pack(fill=BOTH)
        self.shape_selector = Combobox(self, values=list(self.shapes.keys()))
        self.shape_selector.pack(fill=BOTH)
        Label(self, text="Distance").pack(fill=BOTH)
        self.distance = DoubleVar()
        Entry(self, textvariable=self.distance).pack(fill=BOTH)
        Button(self, text="Save", command=self.save).pack(fill=BOTH)
    
    def save(self) -> None:
        try:
            distance = self.distance.get()
        except (ValueError, TclError):
            messagebox.showerror("Error", "Invalid distance")
            return
        color = self.color_selector.get()
        if color == "": 
            messagebox.showerror("Error", "Select color")
            return
        shape = self.shape_selector.get()
        if shape == "": 
            messagebox.showerror("Error", "Select shape")
            return
        with Session(engine) as session:
            session.add(Route(color=self.colors[color], shape=self.shapes[shape], distance=distance))
            session.commit()
        messagebox.showinfo("Success", "Route successfully added.")
        self.clear()
    
    def clear(self) -> None:
        self.color_selector.set("")
        self.shape_selector.set("")
        self.distance.set(0.0)




engine = create_engine("sqlite:///sopron.sqlite")
MainWindow().mainloop()




