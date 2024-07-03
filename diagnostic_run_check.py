
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
    path = [end]
    while end != start:
        for neighbor in graph[end]:
            if distances[neighbor] + graph[end][neighbor] == distances[end]:
                path = [neighbor] + path
                end = neighbor
                break
    return path

# Example graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2},
    'C': {'A': 3, 'B': 2, 'D': 7},
    'D': {'C': 7}
}

start_node = 'A'
end_node = 'D'

print(f"Shortest path from {start_node} to {end_node}: {shortest_path(graph, start_node, end_node)}")
