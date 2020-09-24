#{
#    'A': ['B', 'C'],
#    'B': ['C', 'D'],
#    'C': ['D'],
#    'D': ['C'],
#    'E': ['F'],
#    'F': ['C'],
#}


class Graph:
    def __init__(self):
        self.graph = {}
        self.nbNodes = 0
    
    def addNode(self,p):
        self.graph[p] = None
    
    def addVertice(self, v1, v2): # addVertice(self, v1, v2) != addVertice(self, v2, v1)
        self.graph[v1] = v2