
import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
        
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))
        
    def dijkstra(self, start, end):
        min_heap = [(0, start)]
        visited = set()
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        
        while min_heap:
            (d, node) = heapq.heappop(min_heap)
            if node in visited:
                continue
                
            if node == end:
                return distances[node]
            
            visited.add(node)
            
            for neighbor, weight in self.edges[node]:
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))
        
        return float('inf')

# Example usage:
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')

g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

print(g.dijkstra('A', 'D'))  # Output: 4
