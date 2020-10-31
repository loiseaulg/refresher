from graph import Graph
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
    """Iterative version of the function above, allowing us to use it on a bigger dataset without any risk of overflow

    Args:
        points (array): the initial list of points
        epsillon (float): distance max between two points

    Returns:
        array: the new trajectory
    """
    index = 0
    while index < len(points) - 1:
        if points[index].distance(points[index + 1]) > epsillon :
            points.insert(index + 1, Point((points[index].x + points[index+1].x)/2, (points[index].y + points[index+1].y)/2))
            index = 0
        else:
            index+=1
    return points

def hybrid_convertTrajectory(points, epsillon):
    """Hybrid version of the convertTrajectory function

    Args:
        points (array): the initial list of points
        epsillon (float): distance max between two points

    Returns:
        array: the new trajectory
    """
    #An exact study of when the trajectory set is said to be expensive could be done, values here are from empirical experiences
    #isTooExpensive = len(points) > 10 and epsillon <= 0.1 or len(points) > 20
    #We will consider here that to be significative for clustering, trajectories must be tall enough, so evevy one of them will be too expensive
    isTooExpensive = True
    if isTooExpensive :
        return convertTrajectory(points, epsillon)
    else :
        return convertTrajectory2(points, epsillon)

def defineBounds(s):
    """defines the boundaries of a set of points, useful for plotting

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
        traj = hybrid_convertTrajectory(traj, epsillon)
        isFirstPoint = True
        lastPoint = None
        for p in traj:
            x = (p.x - p.x%epsillon) + epsillon/2
            y = (p.y - p.y%epsillon) + epsillon/2
            sol.addNode((x,y))
            if not isFirstPoint and lastPoint != (x,y) :
                sol.addEdge(lastPoint,(x,y))
            else :
                isFirstPoint = False
            lastPoint = (x,y)
    return sol