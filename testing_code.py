
from collections import deque

# Function to find the shortest path in a graph using BFS
def shortest_path(graph, start_node, end_node):
    queue = deque([(start_node, [])])
    visited = set()
    
    while queue:
        current_node, path = queue.popleft()
        if current_node == end_node:
            return path + [current_node]
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        for neighbor in graph.get(current_node, []):
            queue.append((neighbor, path + [current_node]))
    
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

start_node = 'A'
end_node = 'F'
shortest_path = shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {end_node}")
