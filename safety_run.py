
from collections import deque

def shortest_path(graph, start, end):
    queue = deque()
    visited = set()
    distance = {start: [start]}
    
    queue.append(start)
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            return distance[node]
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                distance[neighbor] = distance[node] + [neighbor]
    
    return None

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'
path = shortest_path(graph, start, end)

if path:
    print(f"Shortest path from {start} to {end}: {path}")
else:
    print(f"No path found from {start} to {end}")
