import point
import trajectory
import graph
from point import *
from trajectory import Trajectory
import math

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

def trajectory_clustering(initialSet,epsillon):
    convertedSet = []
    for tra in initialSet:
        convertedSet.append(convertTrajectory(tra,epsillon))
    pass

traj = Trajectory.generate_traj(2)
t = Trajectory(points=[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)])
print(defineBounds([[Point(1,1),Point(2,2),Point(3,3),Point(4,4),Point(5,5),Point(6,6)]]))
#######
#print(Trajectory(points=convertTrajectory(t.points,1)))
#traj[index].distance(traj[index + 1])
#print(convertTrajectory(traj.points,10))
#print(traj.points[0].distance(traj.points[1]))
#temp2()