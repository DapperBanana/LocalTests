
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('infinity') for node in graph}
    dist[start] = 0

    while len(pq) > 0:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

for node, dist in shortest_paths.items():
    print(f'Shortest path from {start_node} to {node}: {dist}')
