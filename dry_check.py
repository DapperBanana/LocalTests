
import random

# Generate random maze
def generate_maze(rows, cols):
    maze = [['#']*cols for _ in range(rows)]
    for i in range(1, rows-1, 2):
        for j in range(1, cols-1, 2):
            maze[i][j] = ' '
    for i in range(1, rows-1, 2):
        for j in range(1, cols-1, 2):
            direction = random.choice(['up', 'right', 'down', 'left'])
            if direction == 'up' and i > 1:
                maze[i-1][j] = ' '
            elif direction == 'right' and j < cols-2:
                maze[i][j+1] = ' '
            elif direction == 'down' and i < rows-2:
                maze[i+1][j] = ' '
            elif direction == 'left' and j > 1:
                maze[i][j-1] = ' '
    return maze

# Print maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))
        
# Solve maze using depth-first search
def solve_maze(maze, start, end):
    visited = []
    stack = [start]
    
    while stack:
        current = stack.pop()
        visited.append(current)
        
        if current == end:
            break
        
        neighbors = get_neighbors(current, maze)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
    
    return visited

# Get neighbors of a cell
def get_neighbors(cell, maze):
    neighbors = []
    row, col = cell
    if row > 0 and maze[row-1][col] == ' ':
        neighbors.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] == ' ':
        neighbors.append((row+1, col))
    if col > 0 and maze[row][col-1] == ' ':
        neighbors.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] == ' ':
        neighbors.append((row, col+1))
        
    return neighbors

# Main function
def main():
    rows = 10
    cols = 20
    maze = generate_maze(rows, cols)
    print("Random Maze:")
    print_maze(maze)
    
    start = (1, 1)
    end = (rows-2, cols-2)
    path = solve_maze(maze, start, end)
    
    for cell in path:
        maze[cell[0]][cell[1]] = '.'
    
    print("\nSolved Maze:")
    print_maze(maze)

if __name__ == "__main__":
    main()
