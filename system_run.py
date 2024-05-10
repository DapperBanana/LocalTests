
from collections import defaultdict

def is_tree(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
        return True
    
    if not dfs(1, None):
        return False
    
    return len(visited) == len(graph)

# Example usage
graph = defaultdict(list)
graph[1] = [2, 3]
graph[2] = [1, 4]
graph[3] = [1, 5]
graph[4] = [2, 6]
graph[5] = [3]
graph[6] = [4]

if is_tree(graph):
    print("The graph is a tree.")
else:
    print("The graph is not a tree.")
