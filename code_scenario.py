
# Sample maze to solve
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', 'E', '#']
]

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Function to solve the maze using a simple algorithm
def solve_maze(maze, start):
    stack = [start]
    
    while stack:
        x, y = stack[-1]
        
        if maze[y][x] == 'E':
            return stack
        
        maze[y][x] = '.'
        
        if y > 0 and maze[y-1][x] in (' ', 'E'):
            stack.append((x, y-1))
        elif y < len(maze) - 1 and maze[y+1][x] in (' ', 'E'):
            stack.append((x, y+1))
        elif x > 0 and maze[y][x-1] in (' ', 'E'):
            stack.append((x-1, y))
        elif x < len(maze[0]) - 1 and maze[y][x+1] in (' ', 'E'):
            stack.append((x+1, y))
        else:
            stack.pop()
    
    return None

# Find the starting position
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 'S':
            start = (x, y)
            break

# Solve the maze
solution = solve_maze(maze, start)

# Print the result
if solution:
    print("Solution found:")
    for x, y in solution:
        maze[y][x] = '*'
    print_maze(maze)
else:
    print("No solution found.")
