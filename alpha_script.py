
# Define the maze as a list of strings
maze = [
    "XXXXXXXXXXXXXX",
    "X    X       X",
    "X XX X XXXXX X",
    "X    X X   X X",
    "XXX XX   X X X",
    "X  X  XXXX X X",
    "X XX X X   X X",
    "X    X X XXX X",
    "XXXXXXXXXXXX X"
]

# Define the starting position
start_row = 1
start_col = 0

# Define the goal position
goal_row = 8
goal_col = 13

# Function to print the maze
def print_maze():
    for row in maze:
        print(row)

# Function to check if a position is valid
def is_valid_move(row, col):
    if row < 0 or row >= len(maze):
        return False
    if col < 0 or col >= len(maze[0]):
        return False
    if maze[row][col] == 'X':
        return False
    return True

# Function to solve the maze
def solve_maze(row, col):
    if row == goal_row and col == goal_col:
        return True
    if is_valid_move(row, col):
        maze[row] = maze[row][:col] + 'P' + maze[row][col + 1:]
        if solve_maze(row + 1, col) or solve_maze(row - 1, col) or solve_maze(row, col + 1) or solve_maze(row, col - 1):
            return True
        maze[row] = maze[row][:col] + ' ' + maze[row][col + 1:]
    return False

# Solve the maze starting from the starting position
if solve_maze(start_row, start_col):
    print_maze()
else:
    print("No solution found")
