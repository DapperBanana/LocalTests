
import random
from collections import deque

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    stack = [(0, 0)]
    visited[0][0] = True
    
    while stack:
        current_row, current_col = stack[-1]
        neighbors = [(current_row+1, current_col), (current_row-1, current_col), 
                     (current_row, current_col+1), (current_row, current_col-1)]
        random.shuffle(neighbors)
        
        found = False
        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and not visited[neighbor_row][neighbor_col]:
                maze[current_row][current_col] = ' '
                stack.append((neighbor_row, neighbor_col))
                visited[neighbor_row][neighbor_col] = True
                found = True
                break
        
        if not found:
            stack.pop()
    
    return maze

def find_path(maze):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(0, 0, [])])
    visited = set()
    
    while queue:
        current_row, current_col, path = queue.popleft()
        
        if (current_row, current_col) == (rows-1, cols-1):
            return path + [(current_row, current_col)]
        
        visited.add((current_row, current_col))
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current_row+dr, current_col+dc
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == ' ' and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, path + [(current_row, current_col)]))
    
    return None

if __name__ == '__main__':
    rows, cols = 10, 10
    maze = generate_maze(rows, cols)
    
    print("Random Maze:")
    for row in maze:
        print(' '.join(row))
    
    path = find_path(maze)
    if path:
        print("\nSolution Path:")
        solution = [[' ' for _ in range(cols)] for _ in range(rows)]
        for row, col in path:
            solution[row][col] = '*'
        
        for row in solution:
            print(' '.join(row))
    else:
        print("\nNo solution found.")
