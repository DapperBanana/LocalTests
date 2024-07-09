
import random
from queue import Queue

def generate_maze(rows, cols):
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i % 2 == 0 or j % 2 == 0:
                row.append("#")
            else:
                row.append(" ")
        maze.append(row)

    start_row = random.randint(0, rows//2) * 2
    start_col = random.randint(0, cols//2) * 2
    maze[start_row][start_col] = "S"

    end_row = random.randint(0, rows//2) * 2
    end_col = random.randint(0, cols//2) * 2
    maze[end_row][end_col] = "E"

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = Queue()
    queue.put((1, 1, [(1, 1)]))

    while not queue.empty():
        row, col, path = queue.get()

        if maze[row][col] == "E":
            for step in path:
                maze[step[0]][step[1]] = "."
            return True

        visited[row][col] = True

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + 2*dx, col + 2*dy
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and maze[new_row][new_col] != "#":
                queue.put((new_row, new_col, path + [(new_row, new_col)]))

    return False

ROWS = 21
COLS = 31

maze = generate_maze(ROWS, COLS)
print("Random Maze:")
print_maze(maze)

if solve_maze(maze):
    print("\nSolution:")
    print_maze(maze)
else:
    print("\nNo solution found.")
