
from collections import defaultdict

def bfs_shortest_path(graph, start, end):
    queue = [(start, [start])]
    visited = set([start])

    while queue:
        (node, path) = queue.pop(0)

        for next_node in graph[node]:
            if next_node == end:
                return path + [end]

            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, path + [next_node]))

    return None

# Example graph
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 2, 3]
graph[2] = [0, 1]
graph[3] = [1, 4]
graph[4] = [3]

start_node = 0
end_node = 4

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print("Shortest path from {} to {}: {}".format(start_node, end_node, shortest_path))
else:
    print("No path found from {} to {}".format(start_node, end_node))
