
import heapq

def dijkstra(graph, start):
    # Initialize the distances dictionary with all vertices set to infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Initialize the priority queue with the starting vertex
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If current distance is greater than stored distance, skip
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 3, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'B': 7, 'C': 2}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

for vertex, distance in shortest_distances.items():
    print(f'Shortest distance from {start_vertex} to {vertex} is {distance}')
