
from collections import defaultdict, deque

def shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()

    if start == end:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return new_path
            
            visited.add(node)

    return None


# Example graph
graph = defaultdict(list)
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D', 'E']
graph['C'] = ['A', 'F']
graph['D'] = ['B']
graph['E'] = ['B', 'F']
graph['F'] = ['C', 'E']

start_node = 'A'
end_node = 'F'

path = shortest_path(graph, start_node, end_node)
if path:
    print("Shortest path from", start_node, "to", end_node, ":", path)
else:
    print("No path found from", start_node, "to", end_node)
