
from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def is_tree(self):
        visited = set()
        if self.is_cyclic(-1, 0, visited):
            return False
        
        for i in range(self.nodes):
            if i not in visited:
                return False
        
        return True
        
    def is_cyclic(self, parent, node, visited):
        visited.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited or self.is_cyclic(node, neighbor, visited):
                return True
        
        return False

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 4)

if g.is_tree():
    print("The graph is a tree")
else:
    print("The graph is not a tree")
