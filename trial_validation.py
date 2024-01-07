
import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the distances to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a priority queue to store the nodes to visit
    queue = [(0, start)]

    while queue:
        # Pop the node with the smallest distance from the queue
        current_distance, current_node = heapq.heappop(queue)

        # Skip if the node has already been visited
        if current_distance > distances[current_node]:
            continue

        # Update the distances to the neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter distance is found, update the distance and enqueue the neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for node, distance in distances.items():
    print(f"{node}: {distance}")
