
from collections import defaultdict

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = defaultdict(list)
    
    def add_edge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
        
    def is_cyclic_util(self, node, visited, parent):
        visited[node] = True
        
        for neighbor in self.adj_list[node]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        
        return False
    
    def is_tree(self):
        visited = [False] * self.num_nodes
        
        if self.is_cyclic_util(0, visited, -1):
            return False
        
        for i in range(self.num_nodes):
            if not visited[i]:
                return False
        
        return True

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 4)

if g.is_tree():
    print("The graph is a tree")
else:
    print("The graph is not a tree")
