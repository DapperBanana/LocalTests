
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

def solve_maze(maze, x, y):
    if maze[x][y] == 'E':
        return True
    if maze[x][y] == '#' or maze[x][y] == 'X':
        return False
    
    maze[x][y] = 'X'
    
    # right
    if (y < len(maze)-1 and solve_maze(maze, x, y+1)):
        return True
    # down
    if (x < len(maze)-1 and solve_maze(maze, x+1, y)):
        return True
    # left
    if (y > 0 and solve_maze(maze, x, y-1)):
        return True
    # up
    if (x > 0 and solve_maze(maze, x-1, y)):
        return True
    
    maze[x][y] = ' '
    return False

def print_maze(maze):
    for row in maze:
        print("".join(row))

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                return i, j

start_x, start_y = find_start(maze)
solve_maze(maze, start_x, start_y)
print_maze(maze)
