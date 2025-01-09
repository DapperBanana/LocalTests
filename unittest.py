
from collections import defaultdict, deque

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

def shortest_path(graph, start, end):
    return bfs(graph, start, end)

if __name__ == "__main__":
    graph = defaultdict(list)
    add_edge(graph, 'A', 'B')
    add_edge(graph, 'A', 'C')
    add_edge(graph, 'B', 'D')
    add_edge(graph, 'C', 'E')
    add_edge(graph, 'D', 'E')
    
    start = 'A'
    end = 'E'
    
    shortest_path = shortest_path(graph, start, end)
    print(f"The shortest path from {start} to {end} is: {' -> '.join(shortest_path)}")
