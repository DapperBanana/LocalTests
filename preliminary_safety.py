
import random

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    stack = [(0, 0)]
    while stack:
        current_row, current_col = stack[-1]
        maze[current_row][current_col] = ' '
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        
        made_move = False
        for d_row, d_col in directions:
            new_row = current_row + 2*d_row
            new_col = current_col + 2*d_col
            
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '#':
                maze[current_row + d_row][current_col + d_col] = ' '
                stack.append((new_row, new_col))
                made_move = True
                break
        
        if not made_move:
            stack.pop()
    
    return maze

def find_path(maze):
    rows, cols = len(maze), len(maze[0])
    
    queue = [(0, 0, '')]
    visited = set()
    
    while queue:
        current_row, current_col, path = queue.pop(0)
        
        if current_row == rows-1 and current_col == cols-1:
            return path
        
        visited.add((current_row, current_col))
        
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = current_row + d_row
            new_col = current_col + d_col
            
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == ' ' and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, path + ['R', 'L', 'D', 'U'][d_row*2 + d_col]))
    
    return 'No solution found'

rows = 10
cols = 10
maze = generate_maze(rows, cols)
for row in maze:
    print(''.join(row))

print(find_path(maze))
