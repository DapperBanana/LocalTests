
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_helper(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_helper(i, visited, v):
                    return True
            elif parent != i:
                return True

        return False

    def is_cyclic(self):
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_helper(i, visited, -1):
                    return True

        return False

    def is_tree(self):
        if self.is_cyclic():
            return False

        for i in range(self.V):
            if len(self.graph[i]) > 1:
                return False

        return True

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
print("Is the graph a tree? ", g.is_tree())
