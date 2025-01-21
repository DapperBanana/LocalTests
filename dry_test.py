
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current == end:
            print("Path found!")
            return

        visited.add(current)

        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]) and maze[n_row][n_col] != "#" and neighbor not in visited:
                stack.append(neighbor)

    print("No path found!")

maze = [
    ["#", "S", "#", "#", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", "#", "E", "#"]
]

start = (0, 1)
end = (4, 3)

solve_maze(maze, start, end)
