
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_tree(self):
        visited = set()
        
        def is_cyclic(node, parent):
            visited.add(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if is_cyclic(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            
            return False
        
        if is_cyclic(1, -1):
            return False
        
        return len(visited) == len(self.graph)
        

# Example graph
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

if g.is_tree():
    print("Given graph is a tree")
else:
    print("Given graph is not a tree")
