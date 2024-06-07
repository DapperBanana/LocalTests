
import random

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(1, rows-1, 2):
        for j in range(1, cols-1, 2):
            maze[i][j] = 0
    
    stack = [(1, 1)]
    
    while stack:
        current_cell = stack[-1]
        i, j = current_cell
        
        neighbors = []
        
        if i-2 > 0 and maze[i-2][j] == 1:
            neighbors.append((i-2, j))
        if i+2 < rows and maze[i+2][j] == 1:
            neighbors.append((i+2, j))
        if j-2 > 0 and maze[i][j-2] == 1:
            neighbors.append((i, j-2))
        if j+2 < cols and maze[i][j+2] == 1:
            neighbors.append((i, j+2))
            
        if neighbors:
            next_cell = random.choice(neighbors)
            next_i, next_j = next_cell
            maze[next_i][next_j] = 0
            maze[(i+next_i)//2][(j+next_j)//2] = 0
            stack.append(next_cell)
        else:
            stack.pop()
    
    return maze

def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    stack = [(1, 1)]
    visited = set()
    
    while stack:
        current_cell = stack[-1]
        i, j = current_cell
        
        if i == rows-2 and j == cols-2:
            return stack
        
        visited.add(current_cell)
        
        neighbors = []
        if i-1 > 0 and maze[i-1][j] == 0 and (i-1, j) not in visited:
            neighbors.append((i-1, j))
        if i+1 < rows and maze[i+1][j] == 0 and (i+1, j) not in visited:
            neighbors.append((i+1, j))
        if j-1 > 0 and maze[i][j-1] == 0 and (i, j-1) not in visited:
            neighbors.append((i, j-1))
        if j+1 < cols and maze[i][j+1] == 0 and (i, j+1) not in visited:
            neighbors.append((i, j+1))
            
        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
        else:
            stack.pop()
    
    return "No solution found"

rows = 21
cols = 21

maze = generate_maze(rows, cols)

print("Random Maze:")
for row in maze:
    print(row)

solution = solve_maze(maze)
print("\nSolution:")
if solution != "No solution found":
    for cell in solution:
        i, j = cell
        maze[i][j] = 2
    
    for row in maze:
        print(row)
else:
    print(solution)
