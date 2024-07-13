
import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def min_distance(self, dist, visited):
        min_dist = sys.maxsize
        min_index = -1
        
        for v in range(self.vertices):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v
        
        return min_index
    
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        visited = [False] * self.vertices
        
        for _ in range(self.vertices):
            u = self.min_distance(dist, visited)
            visited[u] = True
            
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and not visited[v] and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
        
        return dist
    
    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for i in range(self.vertices):
            print(i, "\t", dist[i])
    
# Example usage
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
        
distances = g.dijkstra(0)
g.print_solution(distances)
