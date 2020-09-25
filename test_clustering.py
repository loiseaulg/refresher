import pytest
from point import *
from trajectory import *
from graph import *
from clustering import *

def test_single_trajectory():
    t = [Point(1,1),Point(1,2),Point(3,3),Point(4,2)]
    assert trajectory_clustering([t],1) == { '(1,1)': ['(1,2)'], '(1,2)': ['(3,3)'], '(3,3)': ['(4,2)'], '(4,2)':[]}