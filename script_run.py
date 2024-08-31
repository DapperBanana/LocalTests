
import random

def create_maze(width, height):
    maze = [["#"] * (width * 2 + 1) for _ in range(height * 2 + 1)]

    def dfs(x, y):
        maze[y][x] = " "
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 < nx < width * 2 and 0 < ny < height * 2 and maze[ny][nx] == "#":
                maze[y + dy][x + dx] = " "
                dfs(nx, ny)

    dfs(1, 1)
    maze[0][1] = " "
    maze[-1][-2] = " "
    return maze

def solve_maze(maze):
    height, width = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve(x, y):
        if maze[y][x] == " ":
            maze[y][x] = "."
            if x == width - 2 and y == height - 2:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if solve(nx, ny):
                    return True
            maze[y][x] = "-"
        return False

    solve(1, 1)

if __name__ == '__main__':
    width, height = 10, 10
    maze = create_maze(width, height)
    solve_maze(maze)

    for row in maze:
        print("".join(row))
