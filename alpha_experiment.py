
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def is_tree(self):
        visited = set()
        if self.is_cyclic(0, visited, -1):
            return False
 
        for i in range(len(self.graph)):
            if i not in visited:
                return False
 
        return True
 
    def is_cyclic(self, v, visited, parent):
        visited.add(v)
 
        for i in self.graph[v]:
            if i not in visited:
                if self.is_cyclic(i, visited, v):
                    return True
            elif parent != i:
                return True
 
        return False
 
# Test example
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

if g.is_tree():
    print("The graph is a tree")
else:
    print("The graph is not a tree")
