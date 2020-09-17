from math import sqrt

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, o):
        return not (self == o)

    def set_location(self,x,y):
        self.x = x
        self.y = y
        return self

    def translate(self,dx,dy):
        self.x += dx
        self.y += dy
        return self
    
    def distance(self,other):
        return sqrt((self.x-other.x)*(self.x-other.x)+(self.y-other.y)*(self.y-other.y))

    def distance_from_origin(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def __add__(self,o):
        return Point(self.x +  o.x, self.y + o.y)

    def __str__(self):
        return "( "+ str(self.x) +" , "+ str(self.y) +" )"

    
    