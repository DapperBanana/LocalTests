
import random

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            if random.random() < 0.3:  # 30% chance of creating a wall
                maze[row][col] = 1
            
    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    
    while stack:
        row, col = stack.pop()
        if (row, col) == end:
            return True
        
        if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0 and (row, col) not in visited:
            visited.add((row, col))
            
            stack.append((row+1, col))  # Move down
            stack.append((row-1, col))  # Move up
            stack.append((row, col+1))  # Move right
            stack.append((row, col-1))  # Move left
            
    return False

# Main program
rows, cols = 10, 10
start = (0, 0)
end = (rows-1, cols-1)

maze = generate_maze(rows, cols)
print("Generated Maze:")
for row in maze:
    print(row)

print("\nSolving the maze...")
if solve_maze(maze, start, end):
    print("Path found from start to end.")
else:
    print("No path found from start to end.")
