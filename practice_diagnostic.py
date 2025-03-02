
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    while heap:
        (d, current_node) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            if distance[current_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_node] + weight
                heapq.heappush(heap, (distance[neighbor], neighbor))
    
    return distance

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

for node, distance in shortest_distances.items():
    print(f'Shortest distance from node {start_node} to node {node}: {distance}')
