
import random

# function to generate a random maze
def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]

    for i in range(1, height, 2):
        for j in range(1, width, 2):
            maze[i][j] = " "

    for i in range(height):
        maze[i][0] = "#"
        maze[i][-1] = "#"
    
    for j in range(width):
        maze[0][j] = "#"
        maze[-1][j] = "#"

    return maze

# function to print the maze
def print_maze(maze):
    for row in maze:
        print("".join(row))

# function to solve the maze using depth-first search
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        
        if current == end:
            break
        
        visited.add(current)
        
        x, y = current
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            next_x, next_y = x + dx*2, y + dy*2
            if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == " " and (next_x, next_y) not in visited:
                stack.append((next_x, next_y))
                maze[next_x][next_y] = "."

    return maze

# generate a random maze
width, height = 21, 21
start, end = (1, 1), (height-2, width-2)
maze = generate_maze(width, height)

# solve the maze
maze = solve_maze(maze, start, end)

# print the maze
print_maze(maze)
