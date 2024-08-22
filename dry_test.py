
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
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
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return True

        return False

    def is_tree(self):
        if self.is_cyclic():
            return False

        visited = [False] * self.vertices

        if self.is_connected(0, visited) is False:
            return False

        for i in range(self.vertices):
            if not visited[i]:
                return False

        return True

    def is_connected(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.is_connected(i, visited):
                    return True

        return False

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
