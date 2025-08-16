
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)
    
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        
        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        
        return False
    
    def is_tree(self):
        visited = {}
        for v in self.graph:
            visited[v] = False
        
        if self.is_cyclic_util(0, visited, -1):
            return False
        
        for key in visited:
            if not visited[key]:
                return False
        
        return True

# create a graph that is not a tree
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 3)

# create a graph that is a tree
g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(0, 3)
g2.add_edge(1, 2)

print("Is g1 a tree:", g1.is_tree())
print("Is g2 a tree:", g2.is_tree())
