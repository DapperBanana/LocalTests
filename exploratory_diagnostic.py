
from collections import deque

def shortest_path(graph, start, end):
    if start == end:
        return [start]
    
    queue = deque()
    queue.append([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                
                if neighbor == end:
                    return new_path
                
                queue.append(new_path)
    
    return None

# Example graph
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
end_node = 'F'
shortest_path = shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node} is: {shortest_path}")
else:
    print("No path found.")
