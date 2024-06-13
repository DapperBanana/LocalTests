
import random

# Generates a random maze using Prim's algorithm
def generate_maze(rows, cols):
    maze = [['#'] * (cols * 2 + 1) for _ in range(rows * 2 + 1)]
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        maze[y * 2 + 1][x * 2 + 1] = ' '
        
        neighbors = [(x+dx, y+dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= x+dx < cols and 0 <= y+dy < rows]        
        random.shuffle(neighbors)
        
        for nx, ny in neighbors:
            if (nx, ny) not in visited:
                stack.append((nx, ny))
                maze[y+ny+1][x+nx+1] = ' '
    
    return maze

# Solves the maze using depth-first search
def solve_maze(maze):
    rows, cols = len(maze) // 2, len(maze[0]) // 2
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack[-1]
        if (x, y) == (cols-1, rows-1):
            break

        visited.add((x, y))

        found = False
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and maze[y*2+1+dy][x*2+1+dx] == ' ' and (nx, ny) not in visited:
                stack.append((nx, ny))
                found = True
                break
        
        if not found:
            stack.pop()
    
    return stack

# Main program
rows, cols = 10, 10
maze = generate_maze(rows, cols)
solution = solve_maze(maze)

# Print the random maze
for row in maze:
    print(''.join(row))

# Print the solution path
for x, y in solution:
    maze[y*2+1][x*2+1] = 'X'

print("\nSolved maze:")
for row in maze:
    print(''.join(row))
