
from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end:
            return path
        
        for n in graph.get(node, []):
            new_path = list(path)
            new_path.append(n)
            queue.append(new_path)
            
    return None

# Example usage
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

shortest_path = bfs_shortest_path(graph, start, end)
if shortest_path:
    print(f"Shortest path from {start} to {end}: {shortest_path}")
else:
    print(f"No path found from {start} to {end}")
