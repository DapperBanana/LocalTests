
from collections import defaultdict

def is_tree(graph):
    seen = set()
    stack = [(list(graph.keys())[0], None)]
    
    while stack:
        node, parent = stack.pop()
        if node in seen:
            return False
        seen.add(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                stack.append((neighbor, node))
    
    return len(seen) == len(graph)

# Example graph
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}

if is_tree(graph):
    print("The given graph is a tree.")
else:
    print("The given graph is not a tree.")
