
import random

# Initialize maze parameters
width = 20
height = 20
maze = [[0 for _ in range(width)] for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Generate random maze
def generate_maze(x, y):
    visited[y][x] = True
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
            maze[y][x] |= 1 << directions.index((dx, dy))
            maze[ny][nx] |= 1 << directions.index((-dx, -dy))
            generate_maze(nx, ny)

generate_maze(0, 0)

# Depth-first search to solve maze
def solve_maze(x, y):
    if x < 0 or x >= width or y < 0 or y >= height or visited[y][x]:
        return False
    visited[y][x] = True
    if x == width - 1 and y == height - 1:
        return True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if maze[y][x] & (1 << directions.index((dx, dy))) == 0:
            if solve_maze(nx, ny):
                return True
    return False

visited = [[False for _ in range(width)] for _ in range(height)]
solve_maze(0, 0)

# Print maze
for row in maze:
    for cell in row:
        print("{:02x}".format(cell), end=' ')
    print()
