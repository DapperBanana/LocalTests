
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def isTree(self):
        visited = [False] * self.V
        if self.isCyclicUtil(0, visited, -1):
            return False
        for i in range(self.V):
            if not visited[i]:
                return False
        return True

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)

if g.isTree():
    print("Given graph is a tree")
else:
    print("Given graph is not a tree")
