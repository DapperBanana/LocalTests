
from collections import deque

def shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    
    if start == end:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            
            if neighbor == end:
                return new_path
            
            queue.append(new_path)
    
    return None

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

start_node = 'A'
end_node = 'G'

shortest_path_result = shortest_path(graph, start_node, end_node)

if shortest_path_result:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path_result}")
else:
    print(f"No path found from {start_node} to {end_node}")
