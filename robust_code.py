
import random

# Function to create a random maze of given dimensions
def create_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if i % 2 != 0 and j % 2 != 0:
                maze[i][j] = ' '
    
    start_row = random.randint(0, rows//2) * 2
    start_col = random.randint(0, cols//2) * 2
    end_row = random.randint(0, rows//2) * 2
    end_col = random.randint(0, cols//2) * 2
    maze[start_row][start_col] = 'S'
    maze[end_row][end_col] = 'E'
    
    return maze, (start_row, start_col), (end_row, end_col)

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

# Depth-first search algorithm to solve the maze
def dfs(maze, current, end):
    row, col = current
    
    # Check if current cell is the end cell
    if current == end:
        return True
    
    # Check if current cell is a valid cell
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] != ' ':
        return False
    
    # Mark the current cell as visited
    maze[row][col] = '.'
    
    # Explore all possible directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(directions)
    
    for dr, dc in directions:
        if dfs(maze, (row + 2*dr, col + 2*dc), end):
            return True
    
    # If no path found, backtrack
    maze[row][col] = ' '
    
    return False

# Main function to generate and solve the maze
def main(rows, cols):
    maze, start, end = create_maze(rows, cols)
    
    print("Random maze:")
    print_maze(maze)
    
    if dfs(maze, start, end):
        print("\nMaze solved:")
        print_maze(maze)
    else:
        print("\nNo solution found.")

# Generate and solve a random maze of size 10x10
main(10, 10)
