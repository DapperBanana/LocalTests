
import random

# Generate a random maze
def generate_maze(rows, cols):
    maze = [['#']*cols for _ in range(rows)]
    
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            maze[i][j] = ' '
    
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_i = i + direction[0]
            new_j = j + direction[1]
            
            if new_i > 0 and new_i < rows and new_j > 0 and new_j < cols:
                maze[new_i][new_j] = ' '
    
    maze[0][1] = ' '
    maze[rows-1][cols-2] = ' '
    
    return maze

# Depth-first search algorithm to solve the maze
def dfs(maze, current_i, current_j):
    if current_i < 0 or current_i >= len(maze) or current_j < 0 or current_j >= len(maze[0]):
        return False
    
    if maze[current_i][current_j] == ' ':
        maze[current_i][current_j] = '.'
        
        if current_i == 0 or current_i == len(maze)-1 or current_j == 0 or current_j == len(maze[0])-1:
            return True
        
        if dfs(maze, current_i+1, current_j) or dfs(maze, current_i-1, current_j) or dfs(maze, current_i, current_j+1) or dfs(maze, current_i, current_j-1):
            return True
        
        maze[current_i][current_j] = ' '
    
    return False

# Print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Main function
if __name__ == "__main__":
    rows = 10
    cols = 10

    maze = generate_maze(rows, cols)
    print("Generated Maze:")
    print_maze(maze)

    solved = dfs(maze, 1, 0)

    if solved:
        print("\nSolved Maze:")
        print_maze(maze)
        print("\nMaze is solvable!")
    else:
        print("\nMaze is unsolvable!")
