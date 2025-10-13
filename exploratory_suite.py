
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for i in self.edges[v]:
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

        def dfs(v):
            visited[v] = True
            for i in self.edges[v]:
                if not visited[i]:
                    dfs(i)

        dfs(0)

        for i in range(self.vertices):
            if not visited[i]:
                return False

        return True

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

if g.is_tree():
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
