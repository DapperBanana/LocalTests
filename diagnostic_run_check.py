
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for u in self.adj_list[v]:
            if not visited[u]:
                if self.is_cyclic_util(u, visited, v):
                    return True
            elif u != parent:
                return True

        return False

    def is_tree(self):
        visited = [False] * self.num_vertices

        if self.is_cyclic_util(0, visited, -1):
            return False

        for i in range(self.num_vertices):
            if not visited[i]:
                return False

        return True


# Test the graph
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)

if g.is_tree():
    print("Given graph is a tree")
else:
    print("Given graph is not a tree")
