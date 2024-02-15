
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start, end):
        visited = [False] * self.vertices
        queue = deque()
        distance = {}
        parent = {}
        for vertex in self.adjacency_list:
            distance[vertex] = float('inf')
        distance[start] = 0
        queue.append(start)
        visited[start] = True
        while queue:
            current_node = queue.popleft()
            for neighbor in self.adjacency_list[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[current_node] + 1
                    parent[neighbor] = current_node
                    queue.append(neighbor)
                    if neighbor == end:
                        return self.get_shortest_path(parent, start, end)
        return []

    def get_shortest_path(self, parent, start, end):
        path = []
        current_node = end
        while current_node != start:
            path.append(current_node)
            current_node = parent[current_node]
        path.append(start)
        path.reverse()
        return path

# Example usage
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

start_node = 0
end_node = 6
shortest_path = g.bfs(start_node, end_node)
print("Shortest path:", shortest_path)
