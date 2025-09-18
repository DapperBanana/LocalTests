
import random

def generate_maze(rows, columns):
    maze = [['#']*columns for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            if i % 2 != 0 and j % 2 != 0:
                maze[i][j] = ' '
    
    start_row = random.randrange(0, rows, 2)
    start_col = random.randrange(0, columns, 2)
    end_row = random.randrange(0, rows, 2)
    end_col = random.randrange(0, columns, 2)
    
    maze[start_row][start_col] = 'S'
    maze[end_row][end_col] = 'E'
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def solve_maze(maze, start_row, start_col, end_row, end_col):
    if start_row < 0 or start_col < 0 or start_row >= len(maze) or start_col >= len(maze[0]) or maze[start_row][start_col] == '#' or maze[start_row][start_col] == '*':
        return False
    
    maze[start_row][start_col] = '*'
    
    if start_row == end_row and start_col == end_col:
        return True
    
    if solve_maze(maze, start_row+1, start_col, end_row, end_col) or solve_maze(maze, start_row-1, start_col, end_row, end_col) or solve_maze(maze, start_row, start_col+1, end_row, end_col) or solve_maze(maze, start_row, start_col-1, end_row, end_col):
        return True
    
    maze[start_row][start_col] = ' '
    return False

rows = 10
columns = 10

maze = generate_maze(rows, columns)
print('Maze:')
print_maze(maze)

print('\nSolving the maze...\n')
start_row, start_col = 1, 1
end_row, end_col = rows-2, columns-2

if solve_maze(maze, start_row, start_col, end_row, end_col):
    print('Maze solved:')
    print_maze(maze)
else:
    print('No solution found.')
