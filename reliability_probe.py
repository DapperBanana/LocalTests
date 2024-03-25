
import random

# Generates a random maze
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    def dfs(row, col):
        maze[row][col] = ' '
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        
        for dr, dc in directions:
            new_row, new_col = row + 2*dr, col + 2*dc
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '#':
                maze[row + dr][col + dc] = ' '
                dfs(new_row, new_col)
                
    dfs(1, 1)
    return maze

# Solves the maze using depth-first search
def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or maze[row][col] == '#' or visited[row][col]:
            return False
        if maze[row][col] == ' ':
            maze[row][col] = '.'
            visited[row][col] = True
            if (row == 1 and col == 1) or dfs(row - 1, col) or dfs(row + 1, col) or dfs(row, col - 1) or dfs(row, col + 1):
                return True
            maze[row][col] = ' '
        return False
    
    dfs(rows - 2, cols - 2)
                
# Main program
rows, cols = 10, 10
maze = generate_maze(rows, cols)
solve_maze(maze)

print("Maze:")
for row in maze:
    print(' '.join(row))
