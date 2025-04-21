
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self.graph[node]:
                queue.append((neighbor, path + [neighbor]))

        return None

# Create a graph
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)

start = 1
end = 3
shortest_path = g.bfs_shortest_path(start, end)

if shortest_path:
    print(f"Shortest path from {start} to {end}: {shortest_path}")
else:
    print(f"No path found from {start} to {end}")
