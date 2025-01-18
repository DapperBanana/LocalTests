
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def shortest_path(graph, start, end):
    distances = dijkstra(graph, start)
    path = []
    current_node = end

    while current_node != start:
        path.insert(0, current_node)
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                current_node = neighbor

    path.insert(0, start)

    return path

# Example
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
end = 'D'

path = shortest_path(graph, start, end)
print("Shortest path:", ' -> '.join(path))
