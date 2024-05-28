
# Define the maze as a 2D list of characters
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Function to solve the maze using Depth First Search
def solve_maze(maze, start, end):
    stack = [start]
    while stack:
        x, y = stack[-1]
        if (x, y) == end:
            print("Found the end of the maze!")
            return True
        if maze[x][y] == ' ':
            maze[x][y] = '.'
            if x+1 < len(maze) and maze[x+1][y] != '#':
                stack.append((x+1, y))
            if x-1 >= 0 and maze[x-1][y] != '#':
                stack.append((x-1, y))
            if y+1 < len(maze[0]) and maze[x][y+1] != '#':
                stack.append((x, y+1))
            if y-1 >= 0 and maze[x][y-1] != '#':
                stack.append((x, y-1))
        else:
            stack.pop()
    print("No solution found.")
    return False

# Find the start and end points in the maze
start = (1, 1)
end = (6, 8)

# Solve the maze
if solve_maze(maze, start, end):
    print_maze(maze)
