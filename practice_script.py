
import random

# Maze dimensions
WIDTH = 10
HEIGHT = 10

# Maze generation using recursive backtracking algorithm
def generate_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 0

    def backtrack(x, y):
        maze[y][x] = 1
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                maze[(y + ny) // 2][(x + nx) // 2] = 1
                backtrack(nx, ny)

    backtrack(0, 0)
    maze[0][0] = maze[height - 1][width - 1] = 1

    return maze

# A* algorithm for maze solving
def solve_maze(maze):
    start = (0, 0)
    end = (len(maze[0]) - 1, len(maze) - 1)

    open_list = [start]
    closed_list = []
    parent_map = {start: None}

    while open_list:
        current = open_list[0]
        open_list = open_list[1:]

        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent_map[current]
            return path[::-1]

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 1 and (nx, ny) not in closed_list:
                open_list.append((nx, ny))
                parent_map[(nx, ny)] = current
                closed_list.append((nx, ny))

    return None

# Generate and solve a random maze
maze = generate_maze(WIDTH, HEIGHT)
solution = solve_maze(maze)

if solution:
    print("Maze:")
    for row in maze:
        print(row)
    print("Solution:")
    for x, y in solution:
        maze[y][x] = 2
    for row in maze:
        print(row)
else:
    print("No solution found")
