
from collections import deque

def shortest_path(graph, start, end):
    if start not in graph or end not in graph:
        return None

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == end:
            return path
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'
result = shortest_path(graph, start, end)

if result:
    print(f"Shortest path from {start} to {end}: {result}")
else:
    print(f"No path found from {start} to {end}")
