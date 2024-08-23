
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        
        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif i != parent:
                return True
        
        return False
    
    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True
        
        return False
    
    def is_tree(self):
        if self.is_cyclic():
            return False
        
        visited = {node: False for node in self.graph}
        
        if self.is_tree_util(0, visited, -1):
            return False
        
        for val in visited.values():
            if not val:
                return False
        
        return True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

if g.is_tree():
    print("Given graph is a tree")
else:
    print("Given graph is not a tree")
