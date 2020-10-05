from graph import Graph
import point
import trajectory
import graph
from point import *
from trajectory import Trajectory
import math
import numpy as np

""" Increases the recursion Limit of Python"""
import sys
sys.setrecursionlimit(10000)

def convertTrajectory2(points, epsillon, index=0):
    """adds points in a trajectory such that each point is at most at epsillon from the other

    Args:
        points (array): the initial list of points
        epsillon (float): distance max between two points
        index (int, optional): only useful for recursion. Defaults to 0.

    Returns:
        array: the new trajectory
    """
    if index >= len(points) - 1 :
        return points
    else:
        if points[index].distance(points[index + 1]) > epsillon :
            points.insert(index + 1, Point((points[index].x + points[index+1].x)/2, (points[index].y + points[index+1].y)/2))
            convertTrajectory(points,epsillon,index=0)
        else:
            convertTrajectory(points,epsillon,index=index + 1)
        return points

def convertTrajectory(points, epsillon):
    index = 0
    while index < len(points) - 1:
        if points[index].distance(points[index + 1]) > epsillon :
            points.insert(index + 1, Point((points[index].x + points[index+1].x)/2, (points[index].y + points[index+1].y)/2))
            index = 0
        else:
            index+=1
    return points

def defineBounds(s):
    """defines the boundaries of a set of points

    Args:
        s (array): set of multiple trajectories

    Returns:
        [float, float, float, float]: respectively top, bottom, left, right bound
    """
    top, bottom, left, right = -math.inf, math.inf, math.inf, -math.inf
    for traj in s:
        for point in traj:
            if point.x < left :
                left = point.x
            if point.x > right :
                right = point.x
            if point.y > top :
                top = point.y
            if point.y < bottom :
                bottom = point.y
    return [top, bottom, left, right]

def trajectory_clustering(s,epsillon):
    """clusters trajectories from a radius epsillon

    Args:
        s (array): initial set of trajectories
        epsillon (float): clustering radius

    Returns:
        graph : output graph
    """
    sol = Graph()
    for traj in s :
        traj = convertTrajectory(traj, epsillon)
        isFirstPoint = True
        lastPoint = None
        for p in traj:
            x = (p.x - p.x%epsillon) + epsillon/2
            y = (p.y - p.y%epsillon) + epsillon/2
            sol.addNode((x,y))
            if not isFirstPoint and lastPoint != (x,y) :
                sol.addVertice(lastPoint,(x,y))
            else :
                isFirstPoint = False
            lastPoint = (x,y)
    #print(sol.graph)
    return sol

#traj = Trajectory.generate_traj(2)
#t = Trajectory(points=[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)])
#s = [[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)],[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)],
#[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)],[Point(1,1),Point(15,15)]]
#[Point(1.2,1.2),Point(2.2,2.2),Point(3.2,3.2),Point(4.2,4.2),Point(5.2,5.2),Point(6.2,6.2)],
  #  [Point(10.2,10.2),Point(2.2,2.2),Point(50,50),Point(4.1,4.7),Point(0,0),Point(4.1,4.7),Point(0,0)]

      #bounds = defineBounds(s)
    #top, bottom, left, right = bounds[0], bounds[1], bounds[2], bounds[3]
    #vert = np.arange(bottom,top,epsillon)
    #hor = np.arange(left,right,epsillon)