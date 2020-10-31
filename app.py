from parsing import *
from clustering import *
from trajectory import *
import matplotlib.pyplot as plt
import numpy as np

def plotGraph(graph):
    """Plot a result graph of trajectories using Matplotlib

    Args:
        graph (dictionnary)
    """
    for key in graph:
        for p in graph[key]:
            x = [key[0],p[0]]
            y = [key[1],p[1]]
            plt.plot(x,y,color='g')
            plt.title("Clustered trajectories")

def plotData(data):
    """Plot original trajectories (pre-processed)

    Args:
        data (array)
    """
    for traj in data:
        x = []
        y = []
        for p in traj:
            x.append(p.x)
            y.append(p.y)
        plt.plot(x,y,color='r')
        plt.title("Raw trajectories")

class App():
    """Main class for our application
    """
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