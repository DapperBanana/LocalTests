
def is_tree(graph):
    # Check if the graph is connected
    if not is_connected(graph):
        return False
    
    # Check if the graph has no cycles
    if has_cycles(graph):
        return False
    
    return True

def is_connected(graph):
    visited = set()
    stack = [list(graph.keys())[0]]

    while stack:
        node = stack.pop()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited) == len(graph)

def has_cycles(graph):
    visited = set()
    stack = [list(graph.keys())[0]]
    parent = {list(graph.keys())[0]: None}

    while stack:
        node = stack.pop()

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = node
            elif parent[node] != neighbor:
                return True
    
    return False

# Example graph
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

if is_tree(graph):
    print("The graph is a tree.")
else:
    print("The graph is not a tree.")
