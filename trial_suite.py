
import random

def generate_maze(size):
    maze = [[1 for _ in range(2*size+1)] for _ in range(2*size+1)]
    
    for i in range(2*size+1):
        maze[i][0] = 0
        maze[i][-1] = 0
        maze[0][i] = 0
        maze[-1][i] = 0
    
    stack = [(1, 1)]
    visited = set()
    
    while stack:
        current = stack[-1]
        visited.add(current)
        x, y = current
        
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        unvisited_neighbors = [n for n in neighbors if n not in visited]
        
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            nx, ny = next_cell
            dx = nx - x
            dy = ny - y
            maze[x+dx//2][y+dy//2] = 0
            stack.append(next_cell)
        else:
            stack.pop()
    
    maze[1][0] = 0
    maze[2*size-1][2*size] = 0
    
    return maze

def solve_maze(maze):
    stack = [(1, 1)]
    visited = set()
    
    while stack:
        current = stack[-1]
        visited.add(current)
        x, y = current
        
        if x == 2*len(maze)-2 and y == 2*len(maze)-2:
            break
        
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if maze[nx][ny] == 0 and (nx, ny) not in visited]
        
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            stack.append(next_cell)
        else:
            stack.pop()
    
    return stack

size = 10
maze = generate_maze(size)

for row in maze:
    print(''.join(['#' if cell == 1 else ' ' for cell in row]))

solution = solve_maze(maze)

for cell in solution:
    x, y = cell
    maze[x][y] = 2

print("\nSolution:")
for row in maze:
    print(''.join(['#' if cell == 1 else ' ' if cell == 0 else 'X' for cell in row]))
