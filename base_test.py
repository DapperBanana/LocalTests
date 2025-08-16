
import random

# Function to generate a random maze using a depth-first search algorithm
def generate_maze(width, height):
    maze = [[0 for i in range(width)] for j in range(height)]
    stack = [(0, 0)]

    while stack:
        x, y = stack[-1]
        maze[y][x] = 1

        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbors)

        next_x, next_y = None, None
        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                next_x, next_y = nx, ny
                break

        if next_x is not None:
            stack.append((next_x, next_y))
            maze[(y+next_y)//2][(x+next_x)//2] = 1
        else:
            stack.pop()

    return maze

# Function to find the solution to the maze using depth-first search
def find_solution(maze, start, end):
    width = len(maze[0])
    height = len(maze)
    visited = [[False for i in range(width)] for j in range(height)]

    def dfs(x, y):
        if x == end[0] and y == end[1]:
            return [(x, y)]

        visited[y][x] = True

        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        random.shuffle(neighbors)

        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1 and not visited[ny][nx]:
                path = dfs(nx, ny)
                if path is not None:
                    return [(x, y)] + path
        
        return None

    return dfs(start[0], start[1])

# Generate a random maze
maze = generate_maze(11, 11)

# Find the solution to the maze
start = (1, 1)
end = (9, 9)
solution = find_solution(maze, start, end)

# Print the maze
for row in maze:
    print("".join(["#" if cell == 0 else " " for cell in row]))

# Print the solution
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if (x, y) in solution:
            print(".", end="")
        else:
            print("#" if cell == 0 else " ", end="")
    print()
