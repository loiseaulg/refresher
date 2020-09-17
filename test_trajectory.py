from trajectory import *
from point import *
import pytest

#=======================================
def test_void_trajectory():
    assert len(Trajectory()) == 0

def test_add_point_to_trajectory():
    t1 = Trajectory([Point(1,1),Point(1,2)])
    p = Point(1,3)
    assert t1.add_Point(p).points == [Point(1,1),Point(1,2),Point(1,3)] 

def test_remove_point_to_trajectory():
    t1 = Trajectory([Point(1,1),Point(1,2)])
    p = Point(1,2)
    assert t1.remove_Point(p).points == [Point(1,1)]

def test_add_multiple_points():
    t1 = Trajectory([Point(1,1),Point(1,2)])
    l = [Point(3,3),Point(4,2)]
    assert t1.add_Points(l).points == [Point(1,1),Point(1,2),Point(3,3),Point(4,2)]

def test_remove_multiple_points():
    t1 = Trajectory([Point(1,1),Point(3,3),Point(4,2)])
    l = [Point(3,3),Point(4,2)]
    assert t1.remove_Points(l).points == [Point(1,1)]

def test_concat():
    t1 = Trajectory([Point(1,1),Point(2,2),Point(3,3)])
    t2 = Trajectory([Point(4,4),Point(5,5),Point(6,6)])
    assert t1.concat(t2).points == [Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)]


