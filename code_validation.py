
import random

# Generate a random maze using Depth First Search algorithm
def generate_maze(rows, cols):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(row, col):
        maze[row][col] = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for d_row, d_col in directions:
            new_row, new_col = row + 2*d_row, col + 2*d_col
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0:
                maze[row + d_row][col + d_col] = 1
                dfs(new_row, new_col)

    dfs(0, 0)
    return maze

# Find the solution to the maze using Breadth First Search algorithm
def find_solution(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    end = (rows-1, cols-1)

    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)

        if current == end:
            return path

        visited.add(current)

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = current[0] + dr, current[1] + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))

    return None

# Set the maze size
rows, cols = 10, 10

# Generate a random maze
maze = generate_maze(rows, cols)

# Find the solution to the maze
solution = find_solution(maze)

# Print the maze
for row in maze:
    print(''.join(['#' if cell == 1 else ' ' for cell in row]))

# Print the solution path
if solution:
    for row in maze:
        print(''.join(['#' if cell == 1 and (i, j) in solution else ' ' for j, cell in enumerate(row)])
else:
    print("No solution found")
