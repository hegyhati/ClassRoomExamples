class Area:
    width=300
    height=300
    
    def __init__(self, width: int, height: int) -> None:
        self.width=width
        self.height=height
        

class Person:
    velocity = (0,0) 
    position = (0,0)
    area=None
    state="healthy"

    def __init__(self, area, position: tuple, velocity: tuple) -> None:
        self.area=area
        self.position=position
        self.velocity=velocity
        
    
    def move(self):
        new_position = [self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]]
        if new_position[0] > self.area.width :
            new_position[0] = self.area.width - (new_position[0]-self.area.width)
            self.velocity=(self.velocity[0] * (-1), self.velocity[1])
        elif new_position[0] < 0 :
            new_position[0] *= (-1)
            self.velocity=(self.velocity[0] * (-1), self.velocity[1])
        if new_position[1] > self.area.height :
            new_position[1] = self.area.height - (new_position[1]-self.area.height)
            self.velocity=(self.velocity[0], (-1) * self.velocity[1])
        elif new_position[1] < 0 :
            new_position[1] *= (-1)
            self.velocity=(self.velocity[0], (-1) * self.velocity[1])
        self.position=tuple(new_position)
        if self.is_infected():
            self.time_until_recovered -= 1
            if self.time_until_recovered == 0:
                self.state="recovered"

    def infect(self):
        if self.state == "healthy":
            self.state="infected"
            self.time_until_recovered=50
    
    def is_infected(self):
        return self.state=="infected"
    
    def is_recovered(self):
        return self.state=="recovered"
    

    
    def distance_from(self, other) -> float:
        return ((self.position[0]-other.position[0]) ** 2 + (self.position[1]-other.position[1]) ** 2) ** 0.5

