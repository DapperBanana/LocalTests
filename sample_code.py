
import random

def generate_maze(width, height):
    maze = []
    for i in range(height):
        row = ['#' if random.random() < 0.3 else ' ' for j in range(width)]
        maze.append(row)
    return maze

def solve_maze(maze, x, y):
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze) or maze[y][x] == '#':
        return False
    if maze[y][x] == 'X':
        return True
    maze[y][x] = 'V'
    if solve_maze(maze, x+1, y) or solve_maze(maze, x-1, y) or solve_maze(maze, x, y+1) or solve_maze(maze, x, y-1):
        maze[y][x] = 'X'
        return True
    return False

def print_maze(maze):
    for row in maze:
        print(''.join(row))

width = 10
height = 10
maze = generate_maze(width, height)
maze[0][0] = ' '
maze[height-1][width-1] = 'X'

print("Generated maze:")
print_maze(maze)

solve_maze(maze, 0, 0)

print("\nSolved maze:")
print_maze(maze)
