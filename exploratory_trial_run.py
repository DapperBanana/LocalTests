
import random

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    stack = []
    start_row, start_col = random.randint(0, rows-1), random.randint(0, cols-1)
    stack.append((start_row, start_col))
    maze[start_row][start_col] = ' '
    
    while stack:
        current_row, current_col = stack[-1]
        neighbors = [(current_row-2, current_col), (current_row+2, current_col), 
                     (current_row, current_col-2), (current_row, current_col+2)]
        random.shuffle(neighbors)
        
        found = False
        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and maze[neighbor_row][neighbor_col] == '#':
                maze[(current_row + neighbor_row) // 2][(current_col + neighbor_col) // 2] = ' '
                maze[neighbor_row][neighbor_col] = ' '
                stack.append((neighbor_row, neighbor_col))
                found = True
                break
        
        if not found:
            stack.pop()
    
    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    
    while stack:
        current_row, current_col = stack.pop()
        if (current_row, current_col) in visited:
            continue
        
        visited.add((current_row, current_col))
        
        if (current_row, current_col) == end:
            print("Maze solved!")
            break
        
        neighbors = [(current_row-1, current_col), (current_row+1, current_col),
                     (current_row, current_col-1), (current_row, current_col+1)]
        
        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and maze[neighbor_row][neighbor_col] == ' ':
                stack.append((neighbor_row, neighbor_col))
    
    if (current_row, current_col) != end:
        print("Maze cannot be solved.")
    
    return visited

# Main code
rows, cols = 21, 21
maze = generate_maze(rows, cols)
start, end = (1, 1), (rows-2, cols-2)

for row in maze:
    print(''.join(row))

print("Solving the maze...")
visited = solve_maze(maze, start, end)

for row in range(rows):
    for col in range(cols):
        if maze[row][col] == ' ':
            if (row, col) in visited:
                maze[row][col] = '.'
            else:
                maze[row][col] = 'o'

for row in maze:
    print(''.join(row))
