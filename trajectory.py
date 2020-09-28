from point import *
from random import randint

class Trajectory:
    def __init__(self, points = []):
        self.points = points

    def __len__(self):
        return len(self.points)
    
    def __str__(self):
        string = ''
        for p in self.points:
            string+= str(p) + '; '
        return '[' + string + ']'
    
    def add_Point(self,point):
        self.points.append(point)
        return self
    
    def add_Points(self,array):
        for p in array:
            self.add_Point(p)
        return self

    def remove_Point(self,point):
        self.points.remove(point)
        return self
    
    def remove_Points(self,array):
        for p in array:
            self.remove_Point(p)
        return self
    
    def concat(self,o):
        self.points += o.points
        return self
    
    @staticmethod
    def generate_traj(n):
        temp = []
        for i in range(n):
            temp.append(Point(randint(0,50),randint(0,50)))
        return Trajectory(points = temp)

