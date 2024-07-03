
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            current_node = min(
                (node for node in self.graph if node not in visited),
                key=lambda node: distances[node]
            )

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return distances

    def shortest_path(self, start, end):
        distances = self.dijkstra(start)
        path = [end]
        current_node = end

        while current_node != start:
            for neighbor, weight in self.graph[current_node].items():
                if distances[current_node] - weight == distances[neighbor]:
                    path.append(neighbor)
                    current_node = neighbor
                    break

        return distances[end], list(reversed(path))

# Example Usage
g = Graph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 4)

print("Shortest path from A to E:", g.shortest_path('A', 'E'))
