#{
#    'A': ['B', 'C'],
#    'B': ['C', 'D'],
#    'C': ['D'],
#    'D': ['C'],
#    'E': ['F'],
#    'F': ['C'],
#}

"""TODO:
* Add possibility to create a graph from a trajectory
"""
class Graph:
    def __init__(self, fromList=None):
        if fromList == None :
            self.graph = {}
        else:
            self.graph = {}
        self.nbNodes = 0
    
    def addNode(self,p):
        self.graph[p] = None
        self.nbNodes += 1
    
    def addVertice(self, v1, v2): # addVertice(self, v1, v2) != addVertice(self, v2, v1)
        self.graph[v1] = v2
    
    def removeVertice(self, v):
        self.graph[v] = self.graph[v].remove(v)
    
    def removeNode(self,p):
        del self.graph[p]
        for keys in self.graph.keys:
            self.graph[keys].remove(p)
