
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

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

    def is_tree(self):
        visited = [False] * self.V

        if self.is_cyclic_util(0, visited, -1):
            return False

        for i in range(self.V):
            if not visited[i]:
                return False

        return True

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 4)

if g.is_tree():
    print("The given graph is a tree")
else:
    print("The given graph is not a tree")
