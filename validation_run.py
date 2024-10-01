
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def is_valid_move(maze, x, y):
    return x >= 0 and x < len(maze[0]) and y >= 0 and y < len(maze) and maze[y][x] != '#'

def solve_maze(maze):
    stack = [(1, 1)]
    while stack:
        x, y = stack[-1]

        if maze[y][x] == ' ':
            maze[y][x] = 'X'
            print_maze(maze)
            print()

        if maze[y][x] == ' ':
            return True

        next_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        stack.pop()
        for move in next_moves:
            if is_valid_move(maze, move[0], move[1]):
                stack.append(move)

    return False

if solve_maze(maze):
    print("Maze solved!")
else:
    print("No solution found!")
