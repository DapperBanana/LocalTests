
import random

def generate_maze(rows, cols):
    maze = [['X' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.3:
                maze[i][j] = ' '
    
    maze[0][0] = 'S'
    maze[rows-1][cols-1] = 'E'
    
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def solve_maze_dfs(maze, row, col):
    rows = len(maze)
    cols = len(maze[0])
    
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False
    
    if maze[row][col] == 'E':
        return True
    
    if maze[row][col] != ' ':
        return False
    
    maze[row][col] = '.'
    
    if solve_maze_dfs(maze, row+1, col) or solve_maze_dfs(maze, row-1, col) or solve_maze_dfs(maze, row, col+1) or solve_maze_dfs(maze, row, col-1):
        return True
    
    maze[row][col] = ' '
    
    return False

rows = 10
cols = 10

maze = generate_maze(rows, cols)
print("Generated Maze:")
print_maze(maze)

print("\nSolving Maze:")
if solve_maze_dfs(maze, 0, 0):
    print_maze(maze)
    print("\nMaze solved successfully!")
else:
    print("No solution found.")

