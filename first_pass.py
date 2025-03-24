
import random
from collections import deque

def generate_maze(width, height):
    maze = [['#'] * (2*width + 1) for _ in range(2*height + 1)]
    nodes = [(i, j) for i in range(height) for j in range(width)]
    stack = []
    starting_node = random.choice(nodes)
    stack.append(starting_node)
    visited = set([starting_node])

    def neighbors(node):
        i, j = node
        if i > 0 and (i-1, j) not in visited:
            yield (i-1, j)
        if i < height - 1 and (i+1, j) not in visited:
            yield (i+1, j)
        if j > 0 and (i, j-1) not in visited:
            yield (i, j-1)
        if j < width - 1 and (i, j+1) not in visited:
            yield (i, j+1)

    while stack:
        current_node = stack[-1]
        unvisited_neighbors = [neighbor for neighbor in neighbors(current_node)]
        if unvisited_neighbors:
            next_node = random.choice(unvisited_neighbors)
            visited.add(next_node)
            maze[2*current_node[0] + 1 + next_node[0]][2*current_node[1] + 1 + next_node[1]] = ' '
            stack.append(next_node)
        else:
            stack.pop()

    return maze

def solve_maze(maze, start, end):
    height = len(maze)
    width = len(maze[0])
    visited = set()
    queue = deque([(start, [])])

    def neighbors(node):
        i, j = node
        if i > 0 and maze[2*i][2*j + 1] == ' ' and (i-1, j) not in visited:
            yield (i-1, j)
        if i < height - 1 and maze[2*i + 2][2*j + 1] == ' ' and (i+1, j) not in visited:
            yield (i+1, j)
        if j > 0 and maze[2*i + 1][2*j] == ' ' and (i, j-1) not in visited:
            yield (i, j-1)
        if j < width - 1 and maze[2*i + 1][2*j + 2] == ' ' and (i, j+1) not in visited:
            yield (i, j+1)

    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)

        if current_node == end:
            return path + [current_node]

        for neighbor in neighbors(current_node):
            queue.append((neighbor, path + [current_node]))

    return []

def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == '__main__':
    width = 10
    height = 10
    maze = generate_maze(width, height)
    print("Random Maze:")
    print_maze(maze)

    start = (0, 0)
    end = (height - 1, width - 1)
    solution = solve_maze(maze, start, end)
    
    if not solution:
        print("No solution found.")
    else:
        for node in solution:
            maze[2*node[0] + 1][2*node[1] + 1] = 'S'
        maze[1][0] = 'S'
        maze[2*end[0] + 1][2*end[1] + 1] = 'E'
        print("\nSolution:")
        print_maze(maze)
