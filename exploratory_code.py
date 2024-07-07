
from collections import defaultdict, deque

def shortest_path(graph, start, end):
    queue = deque()
    visited = set()
    
    queue.append((start, [start]))
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node == end:
            return path
        
        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
    
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
print(f"Shortest path from node {start_node} to node {end_node}: {shortest_path}")
