from graph import Graph
import point
import trajectory
import graph
from point import *
from trajectory import Trajectory
import math
import numpy as np

import sys
sys.setrecursionlimit(10000)

def convertTrajectory(points, epsillon, index=0):
    if index >= len(points) - 1 :
        return points
    else:
        if points[index].distance(points[index + 1]) > epsillon :
            points.insert(index + 1, Point((points[index].x + points[index+1].x)/2, (points[index].y + points[index+1].y)/2))
            convertTrajectory(points,epsillon,index=0)
        else:
            convertTrajectory(points,epsillon,index=index + 1)
        return points

def defineBounds(s):
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

def temp(s,epsillon):
    sol = Graph()
    for traj in s :
        traj = convertTrajectory(traj, 0.5)
    #bounds = defineBounds(s)
    #top, bottom, left, right = bounds[0], bounds[1], bounds[2], bounds[3]
    #vert = np.arange(bottom,top,epsillon)
    #hor = np.arange(left,right,epsillon)
    #for traj in s :
        for p in traj:
            x = (p.x - p.x%epsillon) + epsillon/2
            y = (p.y - p.y%epsillon) + epsillon/2
            sol.addNode((x,y))
            #sol.addNode(Point(x,y)
    #m = np.zeros((len(vert),len(hor)))
    #for i in vert:
    #    for j in hor:
    #print(m)
    print(sol.graph)
    return sol


def trajectory_clustering(initialSet,epsillon):
    convertedSet = []
    for tra in initialSet:
        convertedSet.append(convertTrajectory(tra,epsillon))
    pass

traj = Trajectory.generate_traj(2)
t = Trajectory(points=[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)])
s = [[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)],[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)],
[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)],[Point(1,1),Point(15,15)]
    
]
#[Point(1.2,1.2),Point(2.2,2.2),Point(3.2,3.2),Point(4.2,4.2),Point(5.2,5.2),Point(6.2,6.2)],
  #  [Point(10.2,10.2),Point(2.2,2.2),Point(50,50),Point(4.1,4.7),Point(0,0),Point(4.1,4.7),Point(0,0)]
temp(s,1)

a = 19.3
ep = 0.5
# sol = 9.75
print((a - a%ep) + ep/2)


#######
#print(Trajectory(points=convertTrajectory(t.points,1)))
#traj[index].distance(traj[index + 1])
#print(len(convertTrajectory(traj.points,0.6)))
#print(traj.points[0].distance(traj.points[1]))
#temp2()