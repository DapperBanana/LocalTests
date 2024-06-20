
import random

# Define the maze dimensions
width = 10
height = 10

# Generate a random maze using Prim's algorithm
def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    walls = []
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    maze[start_y][start_x] = 'S'
    walls.append((start_x, start_y))
    
    while walls:
        wall = random.choice(walls)
        x, y = wall
        neighbors = []
        if x > 1: neighbors.append((x - 2, y))
        if x < width - 2: neighbors.append((x + 2, y))
        if y > 1: neighbors.append((x, y - 2))
        if y < height - 2: neighbors.append((x, y + 2))
        
        random_neighbor = random.choice(neighbors)
        nx, ny = random_neighbor
        if maze[ny][nx] == '#':
            maze[ny][nx] = ' '
            maze[y + (ny - y) // 2][x + (nx - x) // 2] = ' '
            walls.append((nx, ny))
        walls.remove(wall)
    
    end_x = random.randint(0, width - 1)
    end_y = random.randint(0, height - 1)
    maze[end_y][end_x] = 'E'
    
    return maze

# Find the solution to the maze using depth-first search
def find_path(maze, x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    if maze[y][x] == '#' or maze[y][x] == 'V':
        return False
    if maze[y][x] == 'E':
        return True
    
    maze[y][x] = 'V'
    
    if find_path(maze, x + 1, y) or find_path(maze, x - 1, y) or find_path(maze, x, y + 1) or find_path(maze, x, y - 1):
        maze[y][x] = 'X'
        return True
    
    return False

# Print the maze and find the solution
maze = generate_maze(width, height)
for row in maze:
    print(' '.join(row))

start_x, start_y = [(i, row.index('S')) for i, row in enumerate(maze) if 'S' in row][0]
find_path(maze, start_x, start_y)
print('\nSolution:')
for row in maze:
    print(' '.join(row))
