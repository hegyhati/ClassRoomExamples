class Vector:
    x=0
    y=0

    def __init__(self, x, y):
        super().__init__()
        self.x=x
        self.y=y
    
    def length(self):
        return (self.x**2 +self.y**2)**0.5
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    def print(self):
        print("({0.x},{0.y})".format(self))

if __name__=='__main__':
    v=Vector(3,4)
    print(v.length())

