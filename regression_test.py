
import heapq

def shortest_path(graph, start, end):
    # Create a priority queue to store vertices based on their shortest distance from the start vertex
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    # Create a dictionary to store the shortest distances from the start vertex to all other vertices
    shortest_distances = {vertex: float('inf') for vertex in graph}
    shortest_distances[start] = 0

    # Create a dictionary to store the previous vertex in the path to each vertex
    previous_vertex = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we found the end vertex, reconstruct the path and return it
        if current_vertex == end:
            path = []
            while previous_vertex[current_vertex]:
                path.insert(0, current_vertex)
                current_vertex = previous_vertex[current_vertex]
            path.insert(0, start)
            return path

        # Check the neighbors of the current vertex and update their shortest distances if necessary
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_vertex[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return None

# Example graph
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 2},
    'D': {}
}

start_vertex = 'A'
end_vertex = 'D'

print(shortest_path(graph, start_vertex, end_vertex))
