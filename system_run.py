
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_tree(self):
        visited = [False] * self.vertices
        if self.is_cyclic(0, visited, -1):
            return False
        
        for i in range(self.vertices):
            if not visited[i]:
                return False
        
        return True

    def is_cyclic(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic(i, visited, v):
                    return True
            elif i != parent:
                return True
        
        return False

# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(0, 4)

if g.is_tree():
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
