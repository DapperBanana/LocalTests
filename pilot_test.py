
import random

# Maze dimensions
WIDTH = 10
HEIGHT = 10

# Generate initial maze with walls everywhere
maze = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Generate random starting point
start_x = random.randint(0, WIDTH - 1)
start_y = random.randint(0, HEIGHT - 1)
maze[start_y][start_x] = 'S'

# Generate random ending point
end_x = random.randint(0, WIDTH - 1)
end_y = random.randint(0, HEIGHT - 1)
maze[end_y][end_x] = 'E'

# Function to check if a cell is valid
def is_valid(x, y):
    return x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT and maze[y][x] != '#'

# Function to get valid neighbors of a cell
def get_neighbors(x, y):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            neighbors.append((new_x, new_y))
    return neighbors

# Depth-first search to solve the maze
def dfs(x, y):
    if maze[y][x] == 'E':
        print("Solved!")
        return True

    maze[y][x] = 'V'  # Mark cell as visited

    neighbors = get_neighbors(x, y)
    random.shuffle(neighbors)
    for nx, ny in neighbors:
        if dfs(nx, ny):
            maze[y][x] = 'X'  # Mark cell as part of solution path
            return True

    return False

# Print initial maze
print("Initial maze:")
for row in maze:
    print(' '.join(row))

# Solve the maze
dfs(start_x, start_y)

# Print solved maze
print("\nSolved maze:")
for row in maze:
    print(' '.join(row))
