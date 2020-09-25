from point import *

"""TODO:
* Add integer trajectory generators
"""
class Trajectory:
    def __init__(self, points = []):
        self.points = points

    def __len__(self):
        return len(self.points)
    
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
