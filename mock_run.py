
from collections import deque

def shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
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
    print(f"The shortest path from {start_node} to {end_node} is: {shortest_path}")
else:
    print("No path found.")
