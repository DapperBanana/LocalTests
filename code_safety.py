
from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    
    if start == end:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            
            if neighbor == end:
                return new_path

    return None

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

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Shortest path between", start_node, "and", end_node, "is:", shortest_path)
else:
    print("There is no path between", start_node, "and", end_node)
