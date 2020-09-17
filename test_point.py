from point import *
from math import sqrt

def test_empty_Point():
    assert Point().x == Point().y == Point(0,0).x == Point(0,0).y == 0

def test_equality():
    assert Point(0,1) != Point(1,0) 

def test_translation():
    p = Point(0,0).translate(3,2)
    assert p.x == 3 and p.y == 2

def test_distance():
    assert Point(0,0).distance(Point(1,1)) == sqrt(2)

def test_distance_origin():
    assert Point(1,1).distance_from_origin() == sqrt(2)