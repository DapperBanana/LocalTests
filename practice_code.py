
import sys

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    
    visited = []
    
    while len(visited) < len(graph.nodes):
        not_visited = {node: distance for node, distance in distances.items() if node not in visited}
        current_node = min(not_visited, key=not_visited.get)
        
        for neighbor, weight in graph.edges[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
        
        visited.append(current_node)
    
    return distances

def shortest_path(graph, start, end):
    distances = dijkstra(graph, start)
    path = [end]
    current_node = end
    
    while current_node != start:
        for neighbor, weight in graph.edges[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                path.insert(0, neighbor)
                current_node = neighbor
                break
    
    return path

# Creating a sample graph
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

start_node = 'A'
end_node = 'D'

path = shortest_path(g, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(path)}")
