
from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end:
            return path
        
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    return None

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['C', 'H'],
    'H': ['F', 'G']
}

start_node = 'A'
end_node = 'H'

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node} is: {' -> '.join(shortest_path)}")
else:
    print("No path found")
