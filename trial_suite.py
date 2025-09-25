
from collections import deque

# Function to find the shortest path using breadth-first search
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
                else:
                    queue.append(new_path)
    
    return None

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting and ending nodes
start_node = 'A'
end_node = 'F'

# Finding the shortest path
shortest_path = shortest_path(graph, start_node, end_node)

print("Shortest path from {} to {}: {}".format(start_node, end_node, shortest_path))
