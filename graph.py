#{
#    'A': ['B', 'C'],
#    'B': ['C', 'D'],
#    'C': ['D'],
#    'D': ['C'],
#    'E': ['F'],
#    'F': ['C'],
#}

class Graph:
    def __init__(self, fromList=None):
        if fromList == None :
            self.graph = {}
            self.nbNodes = 0
        else:
            self.graph = dict(fromList)
            self.nbNodes = len(fromList)
    
    def addNode(self,p):
        if p not in self.graph.keys() :
            self.graph[p] = []
            self.nbNodes += 1
    
    def addVertice(self, v1, v2): # addVertice(self, v1, v2) != addVertice(self, v2, v1)
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)
    
    def removeVertice(self, v):
        self.graph[v] = self.graph[v].remove(v)
    
    def removeNode(self,p):
        del self.graph[p]
        for keys in self.graph.keys:
            self.graph[keys].remove(p)

g = Graph()
g.addNode('A')
g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addVertice('A','C')
g.addVertice('A','C')
print(g.graph)
