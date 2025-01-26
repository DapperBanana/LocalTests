
from collections import deque

# Graph class to represent the graph
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]
        
        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]

    def shortest_path(self, start, end):
        visited = set()
        queue = deque([[start]])
        
        if start == end:
            return [start]
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            
            if node in visited:
                continue
            
            for adjacent in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                
                if adjacent == end:
                    return new_path
            
            visited.add(node)
        
        return None

# Create a graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('D', 'E')
g.add_edge('C', 'F')

# Find the shortest path from 'A' to 'E'
shortest_path = g.shortest_path('A', 'E')
if shortest_path:
    print("Shortest path from 'A' to 'E':", shortest_path)
else:
    print("No path found from 'A' to 'E'")
