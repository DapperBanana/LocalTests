
# Define the maze as a 2D list
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Helper function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Recursive function to solve the maze
def solve_maze(x, y):
    if maze[y][x] == '#':
        return False
    
    if maze[y][x] == 'X':
        return True
    
    maze[y][x] = '.'

    if (solve_maze(x+1, y) or solve_maze(x-1, y) or solve_maze(x, y+1) or solve_maze(x, y-1)):
        maze[y][x] = 'X'
        return True
    
    return False

# Find the start position
start_pos = (1, 1)

# Solve the maze
solve_maze(start_pos[0], start_pos[1])

# Print the solved maze
print_maze(maze)
