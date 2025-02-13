
import random

# Constants for maze
WALL = "#"
EMPTY = " "
START = "S"
END = "E"

# Generate random maze with given dimensions
def generate_maze(width, height):
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    # Make the outer walls
    for i in range(height):
        maze[i][0] = EMPTY
        maze[i][width-1] = EMPTY
    for j in range(width):
        maze[0][j] = EMPTY
        maze[height-1][j] = EMPTY

    # Make random walls
    for i in range(1, height-1):
        for j in range(1, width-1):
            if random.random() < 0.3:
                maze[i][j] = WALL

    # Set start and end points
    maze[1][1] = START
    maze[height-2][width-2] = END

    return maze

# Print the maze
def print_maze(maze):
    for row in maze:
        print("".join(row))

# Solve maze using depth-first search
def solve_maze(maze, x, y):
    if (x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0])):
        return False
    if maze[x][y] == END:
        return True
    if maze[x][y] != EMPTY:
        return False
    
    maze[x][y] = "."
    
    # Try moving in all directions
    if (solve_maze(maze, x+1, y) or solve_maze(maze, x, y+1) or solve_maze(maze, x-1, y) or solve_maze(maze, x, y-1)):
        return True
    
    maze[x][y] = EMPTY
    return False

# Main code
width, height = 10, 10
maze = generate_maze(width, height)

print("Original maze:")
print_maze(maze)

start_x, start_y = 1, 1
solve_maze(maze, start_x, start_y)

print("\nSolved maze:")
print_maze(maze)
