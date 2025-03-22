
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {start: 0}
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node].items():
            new_dist = d + weight
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist

def shortest_path(graph, start, end):
    dist = dijkstra(graph, start)
    path = [end]
    while end != start:
        for neighbor, weight in graph[end].items():
            if dist.get(neighbor, float('inf')) + weight == dist[end]:
                path.append(neighbor)
                end = neighbor
                break
    return list(reversed(path))

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 5},
    'C': {'A': 3, 'B': 1, 'D': 7},
    'D': {'B': 5, 'C': 7}
}

start = 'A'
end = 'D'
path = shortest_path(graph, start, end)
print(f"Shortest path from {start} to {end}: {path}")
