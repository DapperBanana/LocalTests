
# Define the maze as a list of strings
maze = [
    "#####",
    "#S  #",
    "# ###",
    "#   #",
    "### #",
    "#   #",
    "# ###",
    "#   #",
    "#####"
]

# Find the starting position
for i in range(len(maze)):
    if 'S' in maze[i]:
        start_row = i
        start_col = maze[i].index('S')
        break

# Define the movements
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to check if a position is valid
def is_valid(row, col):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
        return False
    if maze[row][col] == '#':
        return False
    return True

# Function to solve the maze
def solve_maze(row, col):
    if maze[row][col] == 'E':
        return True
    for move in movements:
        new_row = row + move[0]
        new_col = col + move[1]
        if is_valid(new_row, new_col):
            maze[row] = maze[row][:col] + ' ' + maze[row][col+1:]
            if solve_maze(new_row, new_col):
                return True
            maze[row] = maze[row][:col] + '#' + maze[row][col+1:]
    return False

# Solve the maze
if solve_maze(start_row, start_col):
    print("Maze solved!")
else:
    print("No solution found.")

# Print the solved maze
for row in maze:
    print(row)
