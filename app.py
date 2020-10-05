from parsing import *
from clustering import *
from trajectory import *
import matplotlib.pyplot as plt

class App():
    def __init__(self,epsillon):
        data = build_trajectory_set()
        graph = trajectory_clustering(data,epsillon=epsillon)
        print(graph.graph)
        for p in graph.graph.keys:
            plt.scatter(p[0],p[1])
        plt.show()

#a = App(0.1)
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
print(trajectory_clustering(build_trajectory_set(),0.1).graph)