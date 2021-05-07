import json
import gear
import ui

with open("bike.json", "rt") as bike_file:
  my_bike = json.load(bike_file)

bike = gear.Bike(my_bike["wheel_radius"], tuple(my_bike["chainring"]),tuple(my_bike["cassette"]))

ui.BikeCalculator(bike).mainloop()
