
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

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

start = 0
end = 5
shortest_path = bfs_shortest_path(graph, start, end)

if shortest_path:
    print(f"Shortest path from {start} to {end}: {shortest_path}")
else:
    print(f"No path found from {start} to {end}")
