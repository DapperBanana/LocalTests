
import random

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    stack = [(0, 0)]
    visited = set()
    
    while stack:
        i, j = stack[-1]
        neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        neighbors = [(x, y) for x, y in neighbors if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited]
        
        if neighbors:
            next_i, next_j = random.choice(neighbors)
            maze[next_i][next_j] = '.'
            stack.append((next_i, next_j))
            visited.add((next_i, next_j))
        else:
            stack.pop()
    
    return maze

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    end = (rows-1, cols-1)
    
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or maze[i][j] == '#' or maze[i][j] == 'X':
            return False
        
        maze[i][j] = 'X'
        
        if (i, j) == end:
            return True
        
        if dfs(i+1, j) or dfs(i-1, j) or dfs(i, j+1) or dfs(i, j-1):
            return True
        
        maze[i][j] = '.'
        return False

    dfs(start[0], start[1])
    
    for row in maze:
        print(' '.join(row))
    
maze = generate_maze(10, 10)
solve_maze(maze)
