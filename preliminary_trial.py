
import random

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = []
    for i in range(2 * rows + 1):
        row = []
        for j in range(2 * cols + 1):
            if i % 2 == 0 or j % 2 == 0:
                row.append("#")
            else:
                row.append(" ")
        maze.append(row)

    stack = [(1, 1)]
    visited = set()
    while stack:
        x, y = stack[-1]
        visited.add((x, y))
        neighbours = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbours)
        unvisited_neighbours = [n for n in neighbours if n not in visited and 0 < n[0] < 2*rows and 0 < n[1] < 2*cols]
        if unvisited_neighbours:
            nx, ny = unvisited_neighbours[0]
            maze[(x + nx) // 2][(y + ny) // 2] = " "
            stack.append(unvisited_neighbours[0])
        else:
            stack.pop()

    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start = (1, 1)
    end = (rows - 2, cols - 2)
    stack = [start]
    visited = set()
    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        if (x, y) == end:
            break
        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbours:
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == " " and (nx, ny) not in visited:
                stack.append((nx, ny))
                visited.add((nx, ny))
                maze[nx][ny] = "."
    return maze

# Generate a random maze with 10 rows and 10 columns
maze = generate_maze(10, 10)

# Solve the maze using depth-first search
solved_maze = solve_maze(maze)

# Print the solved maze
for row in solved_maze:
    print("".join(row))
