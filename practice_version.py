
from queue import Queue

def shortest_path(graph, start, end):
    visited = set()
    q = Queue()
    q.put([start])
    
    while not q.empty():
        path = q.get()
        node = path[-1]
        
        if node == end:
            return path
        
        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                q.put(new_path)
            
            visited.add(node)
    
    return None

graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [5],
    5: []
}

start = 1
end = 5

result = shortest_path(graph, start, end)
if result:
    print(f"Shortest path from {start} to {end}: {result}")
else:
    print(f"No path found from {start} to {end}")
