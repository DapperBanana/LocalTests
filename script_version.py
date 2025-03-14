
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
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    
    return None

# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['E']
}

start_node = 'A'
end_node = 'F'
shortest_path = shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"The shortest path from node {start_node} to node {end_node} is: {' -> '.join(shortest_path)}")
else:
    print(f"No path found from node {start_node} to node {end_node}")
