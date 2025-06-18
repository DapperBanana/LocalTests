
import random

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = []
    for i in range(rows):
        maze.append([])
        for j in range(cols):
            maze[i].append('#')

    stack = [(0, 0)]
    while stack:
        current_cell = stack[-1]
        x, y = current_cell
        maze[y][x] = ' '
        neighbors = []
        if x > 1 and maze[y][x - 2] == '#':
            neighbors.append((x - 2, y))
        if y > 1 and maze[y - 2][x] == '#':
            neighbors.append((x, y - 2))
        if neighbors:
            next_cell = random.choice(neighbors)
            nx, ny = next_cell
            maze[ny][nx] = ' '
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    stack = [start]
    visited = set()
    while stack:
        current_cell = stack.pop()
        if current_cell == end:
            return True
        if current_cell in visited:
            continue
        visited.add(current_cell)
        x, y = current_cell
        neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        for nx, ny in neighbors:
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] != '#' and (nx, ny) not in visited:
                stack.append((nx, ny))
    return False

# Main program
rows = 10
cols = 10
start = (0, 0)
end = (rows - 1, cols - 1)

maze = generate_maze(rows, cols)
for row in maze:
    print(''.join(row))

if solve_maze(maze, start, end):
    print("\nMaze solved!")
else:
    print("\nMaze unsolvable!")
