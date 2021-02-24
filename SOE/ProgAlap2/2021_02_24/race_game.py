from vector_2d import Vector


class Car:
    position=Vector(0,0)
    velocity=Vector(0,0)

    def __init__(self):
        super().__init__()

    def next(self,acceleration):
        if acceleration.x >1 or acceleration.y>1 or acceleration.x <-1 or acceleration.y<-1: 
            raise Exception
        self.velocity = self.velocity + acceleration
        self.position = self.position + self.velocity


c=Car()

while True:
    c.position.print()
    acc=Vector(0,0)
    acc.__setattr__(input("Melyik iranyba gyorsuljak 1-gyel? x/y "),1)
    c.next(acc)
