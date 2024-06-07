
import random

# Generate a random maze
def generate_maze(rows, cols):
    maze = []
    for i in range(rows):
        maze.append(['#' if random.random() < 0.3 else ' ' for _ in range(cols)])
    maze[0][1] = ' ' # start
    maze[-1][-2] = ' ' # end
    return maze

# Print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Solve the maze using depth-first search
def solve_maze_dfs(maze, row, col):
    if maze[row][col] == '#':
        return False
    
    if maze[row][col] == '.':
        return False
    
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
        return False
    
    if maze[row][col] == ' ':
        maze[row][col] = '.'
        if row == len(maze) - 1 and col == len(maze[0]) - 2:
            return True
        if solve_maze_dfs(maze, row - 1, col) or solve_maze_dfs(maze, row + 1, col) or solve_maze_dfs(maze, row, col - 1) or solve_maze_dfs(maze, row, col + 1):
            return True
        maze[row][col] = ' '
        return False

# Generate and solve the maze
maze = generate_maze(10, 20)
print("Generated Maze:")
print_maze(maze)

start_row, start_col = 0, 1
if solve_maze_dfs(maze, start_row, start_col):
    print("\nSolved Maze:")
    print_maze(maze)
else:
    print("No solution found.")
