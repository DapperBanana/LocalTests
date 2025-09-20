
import random

# Maze size
ROWS = 10
COLS = 10

# Generate a random maze using depth-first search algorithm
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]
    visited = set()

    while stack:
        current = stack[-1]
        maze[current[0]][current[1]] = ' '
        visited.add(current)

        neighbors = [(current[0] - 2, current[1]), 
                     (current[0] + 2, current[1]), 
                     (current[0], current[1] - 2), 
                     (current[0], current[1] + 2)]
        
        unvisited_neighbors = [neighbor for neighbor in neighbors 
                               if 0 <= neighbor[0] < rows 
                               and 0 <= neighbor[1] < cols 
                               and neighbor not in visited]
        
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            wall = ((current[0] + next_cell[0]) // 2, 
                    (current[1] + next_cell[1]) // 2)
            maze[wall[0]][wall[1]] = ' '
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

# Depth-first search algorithm to solve the maze
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        current = stack[-1]
        maze[current[0]][current[1]] = 'P'
        visited.add(current)

        if current == end:
            break

        neighbors = [(current[0] - 1, current[1]), 
                     (current[0] + 1, current[1]), 
                     (current[0], current[1] - 1), 
                     (current[0], current[1] + 1)]
        
        valid_neighbors = [neighbor for neighbor in neighbors 
                           if 0 <= neighbor[0] < len(maze) 
                           and 0 <= neighbor[1] < len(maze[0]) 
                           and maze[neighbor[0]][neighbor[1]] != '#' 
                           and neighbor not in visited]
        
        if valid_neighbors:
            next_cell = valid_neighbors[0]
            stack.append(next_cell)
        else:
            maze[current[0]][current[1]] = ' '
            stack.pop()

    return maze

# Print the maze
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Generate and solve the maze
maze = generate_maze(ROWS, COLS)
start = (0, 0)
end = (ROWS - 1, COLS - 1)
solved_maze = solve_maze(maze, start, end)

print("Generated Maze:")
print_maze(maze)

print("\nSolved Maze:")
print_maze(solved_maze)
