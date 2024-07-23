
from collections import defaultdict

def is_tree(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not dfs(neighbor, node):
                    return False
            elif neighbor != parent:
                return False
        return True
    
    if not dfs(0, -1):
        return False
    
    return len(visited) == len(graph)

# Define the graph as an adjacency list
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [0, 3]
graph[2] = [0]
graph[3] = [1]

if is_tree(graph):
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
