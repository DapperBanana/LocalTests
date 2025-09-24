
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start, end):
        visited = [False] * len(self.graph)
        queue = [[start]]
        
        if start == end:
            return [start]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if not visited[node]:
                neighbours = self.graph[node]
                
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    
                    if neighbour == end:
                        return new_path
                
                visited[node] = True
        
        return "No path found"
        
# Creating a graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Finding the shortest path from node 1 to 3
print("Shortest path from node 1 to 3:", g.bfs(1, 3))
