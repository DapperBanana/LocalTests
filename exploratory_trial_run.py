
import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    def create_path(x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2
            
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                maze[y+dy][x+dx] = ' '
                maze[ny][nx] = ' '
                create_path(nx, ny)
    
    maze[1][1] = ' '
    create_path(1, 1)
    
    return maze

def solve_maze(maze, x, y):
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze) or maze[y][x] == '*' or maze[y][x] == '.':
        return False
    
    if maze[y][x] == ' ':
        maze[y][x] = '.'
        
        if x == len(maze[0])-2 and y == len(maze)-2:
            return True
        
        if solve_maze(maze, x+1, y) or solve_maze(maze, x-1, y) or solve_maze(maze, x, y+1) or solve_maze(maze, x, y-1):
            return True
        
        maze[y][x] = '*'
    
    return False

def print_maze(maze):
    for row in maze:
        print(''.join(row))

width = 30
height = 15

maze = generate_maze(width, height)
maze[1][1] = 'S'
maze[height-2][width-2] = 'E'

print("Random Maze:")
print_maze(maze)

solve_maze(maze, 1, 1)

print("\nSolution:")
print_maze(maze)
