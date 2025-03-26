
from collections import defaultdict, deque

def shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node in visited:
            continue

        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

        visited.add(node)
    
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
    print(f"Shortest path from {start_node} to {end_node} is: {' -> '.join(shortest_path)}")
else:
    print(f"No path found from {start_node} to {end_node}")
