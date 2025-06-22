
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

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.is_cyclic(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True

        return False

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

if g.is_tree():
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
