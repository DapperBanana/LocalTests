
from collections import deque

def shortest_path(graph, start, end):
    queue = deque()
    visited = set()
    path = {}
    
    queue.append(start)
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        if node == end:
            shortest_path = []
            while node != start:
                shortest_path.append(node)
                node = path[node]
            shortest_path.append(start)
            shortest_path.reverse()
            return shortest_path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                path[neighbor] = node

    return None

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

shortest_path = shortest_path(graph, start, end)

if shortest_path:
    print(f"The shortest path from {start} to {end} is: {' -> '.join(shortest_path)}")
else:
    print(f"There is no path from {start} to {end}")
