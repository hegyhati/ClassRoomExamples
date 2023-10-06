from threading import Thread
from time import sleep
from math import sin, cos, pi

class Car:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.alpha = pi/2
        self.speed = 0

    def accelerate(self):
        self.speed += 1
    
    def brake(self):
        self.speed *= 0.7
    
    def sleep(self):
        self.y += self.speed * sin(self.alpha)
        self.x += self.speed * cos(self.alpha)
    
    def turn(self, direction:str):
        if direction == "l": self.alpha += pi/18
        elif direction == "r": self.alpha -= pi/18
    
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

mycar = Car()

def global_events():
    global mycar
    while True:
        sleep(1)
        mycar.sleep()
        print(mycar)

Thread(target=global_events, daemon=True).start()

while True:
    action = input()
    if action == "a":
        mycar.accelerate()
    elif action == "b":
        mycar.brake()
    elif action in ["r", "l"]:
        mycar.turn(action)
    