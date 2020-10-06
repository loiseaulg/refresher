from parsing import *
from clustering import *
from trajectory import *
import matplotlib.pyplot as plt
import numpy as np

def plotGraph(graph):
    for key in graph:
        for p in graph[key]:
            x = [key[0],p[0]]
            y = [key[1],p[1]]
            plt.plot(x,y,color='g')

def plotData(data):
    for traj in data:
        x = []
        y = []
        for p in traj:
            x.append(p.x)
            y.append(p.y)
        plt.plot(x,y,color='r')

class App():
    def __init__(self,epsillon):
        data = build_trajectory_set()
        top, bottom, left, right = defineBounds(data)
        plt.axis([left,right,bottom,top])
        graph = trajectory_clustering(data,epsillon=epsillon)
        plt.subplot(121)
        plotGraph(graph.graph)
        plt.subplot(122)
        plotData(data)
        plt.show()

a = App(0.1)
#print(build_trajectory_set())
#data = Trajectory(points=build_trajectory_set())
#print(data)
#graph = trajectory_clustering(data.points,epsillon=1)
#print(graph.graph)
#for p in graph.graph.keys:
#    plt.scatter(p[0],p[1])
#plt.show()
#t = [Point(1,1),Point(1,2),Point(3,3),Point(4,2)]
#print("choco")
#print(build_trajectory_set()[0])
#print(convertTrajectory(build_trajectory_set()[0],1))
#print(convertTrajectory(build_trajectory_set()[0],1))
#print(trajectory_clustering(build_trajectory_set(),0.1).graph)