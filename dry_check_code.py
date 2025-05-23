
import random

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            maze[i][j] = ' '
    
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols and maze[nx][ny] == '#':
                    maze[nx][ny] = ' '
                    maze[i + dx//2][j + dy//2] = ' '
                    break
                
    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    
    while stack:
        curr = stack.pop()
        visited.add(curr)
        
        if curr == end:
            break
        
        x, y = curr
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if nx >= 0 and nx < rows and ny >= 0 and ny < cols and maze[nx][ny] == ' ' and (nx, ny) not in visited:
                stack.append((nx, ny))
    
    return visited

# Main program
rows, cols = 15, 15
start = (1, 1)
end = (rows - 2, cols - 2)

maze = generate_maze(rows, cols)
solution = solve_maze(maze, start, end)

print("Maze:")
for row in maze:
    print(' '.join(row))

print("\nSolution:")
for i in range(rows):
    for j in range(cols):
        if (i, j) in solution:
            print('.', end=' ')
        else:
            print('#', end=' ')
    print()
