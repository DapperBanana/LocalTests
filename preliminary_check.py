
import random

def create_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            if row % 2 != 0 and col % 2 != 0:
                maze[row][col] = ' '
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def solve_maze(maze, start_row, start_col):
    rows, cols = len(maze), len(maze[0])
    stack = [(start_row, start_col)]
    
    while stack:
        row, col = stack.pop()
        
        if maze[row][col] == 'G':
            print("Solved maze:")
            print_maze(maze)
            return True
        
        maze[row][col] = '.'
        
        neighbors = [(row-2, col), (row+2, col), (row, col-2), (row, col+2)]
        random.shuffle(neighbors)
        
        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '.':
                stack.append((r, c))
    
    print("No solution found.")
    return False

def generate_random_maze(rows, cols):
    maze = create_maze(rows, cols)
    
    start_row, start_col = 1, 1
    maze[start_row][start_col] = 'S'
    
    end_row, end_col = rows - 2, cols - 2
    maze[end_row][end_col] = 'G'
    
    solve_maze(maze, start_row, start_col)

if __name__ == '__main__':
    rows, cols = 11, 11
    generate_random_maze(rows, cols)
