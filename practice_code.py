
import random

# Constants
WALL = 'X'
PATH = ' '
START = 'S'
END = 'E'

# Generate random maze
def generate_maze(rows, cols):
    maze = [[WALL for _ in range(cols)] for _ in range(rows)]
    
    # Start and end points
    start = (random.randint(0, rows-1), random.randint(0, cols-1))
    end = (random.randint(0, rows-1), random.randint(0, cols-1))
    
    maze[start[0]][start[1]] = START
    maze[end[0]][end[1]] = END
    
    stack = [start]
    while stack:
        current = stack[-1]
        neighbors = [(current[0]+1, current[1]), (current[0]-1, current[1]), 
                     (current[0], current[1]+1), (current[0], current[1]-1)]
        random.shuffle(neighbors)
        
        connected = False
        for neighbor in neighbors:
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == WALL:
                maze[neighbor[0]][neighbor[1]] = PATH
                stack.append(neighbor)
                connected = True
                break
        
        if not connected:
            stack.pop()
    
    return maze, start, end

# A* algorithm for finding path in maze
def astar(maze, start, end):
    def heuristic(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])
    
    open_set = [(start, 0, heuristic(start))]
    closed_set = []
    
    while open_set:
        current, g, h = min(open_set, key=lambda x: x[1]+x[2])
        if current == end:
            return closed_set + [current]
        
        open_set.remove((current, g, h))
        closed_set.append(current)
        
        for neighbor in [(current[0]+1, current[1]), (current[0]-1, current[1]), 
                         (current[0], current[1]+1), (current[0], current[1]-1)]:
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != WALL and neighbor not in closed_set:
                g = g + 1
                f = g + heuristic(neighbor)
                if (neighbor, g, h) not in open_set:
                    open_set.append((neighbor, g, f))
    
    return None

# Display maze with solution
def display_maze(maze, solution):
    for i in range(len(maze)):
        for j in range(len(maze[0]):
            if (i, j) == solution[0]:
                print('S', end='')
            elif (i, j) == solution[-1]:
                print('E', end='')
            elif (i, j) in solution:
                print('o', end='')
            else:
                print(maze[i][j], end='')
        print()

# Generate random maze
rows = 10
cols = 10
maze, start, end = generate_maze(rows, cols)

# Find solution using A* algorithm
solution = astar(maze, start, end)

# Display maze with solution
display_maze(maze, solution)
