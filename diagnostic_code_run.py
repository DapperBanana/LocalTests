
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for i in self.adj[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True

        return False

    def is_cyclic(self):
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return True

        return False

    def is_tree(self):
        if self.is_cyclic():
            return False

        for i in range(self.V):
            if len(self.adj[i]) > 1:
                return False

        return True

# Example
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

if g.is_tree():
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
