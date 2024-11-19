
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def is_cyclic(self):
        visited = [False] * self.num_nodes
        if self.is_cyclic_util(0, visited, -1):
            return True

        for i in range(1, self.num_nodes):
            if not visited[i]:
                return True

        return False

    def is_connected(self):
        visited = [False] * self.num_nodes
        self.dfs(0, visited)

        for i in range(self.num_nodes):
            if not visited[i]:
                return False

        return True

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def is_tree(self):
        if self.is_cyclic():
            return False

        return self.is_connected()


# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

if g.is_tree():
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
