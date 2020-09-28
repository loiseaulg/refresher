import pytest
from point import *
from trajectory import *
from graph import *
from clustering import *

def test_trajectory_convertion():
    t = Trajectory(points=[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)])
    assert str(Trajectory(points=convertTrajectory(t.points,1))) == '[( 1 , 1 ); ( 1.5 , 1.5 ); ( 2 , 2 ); ( 2.5 , 2.5 ); ( 3 , 3 ); ( 3.5 , 3.5 ); ( 4 , 4 ); ( 4.5 , 4.5 ); ( 5 , 5 ); ( 5.5 , 5.5 ); ( 6 , 6 ); ]'

def test_define_bounds():
    assert defineBounds([[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)]]) == [6, 1, 1, 6]

    
def test_single_trajectory():
    t = [Point(1,1),Point(1,2),Point(3,3),Point(4,2)]
    assert trajectory_clustering([t],1) == { '(1,1)': ['(1,2)'], '(1,2)': ['(3,3)'], '(3,3)': ['(4,2)'], '(4,2)':[]}