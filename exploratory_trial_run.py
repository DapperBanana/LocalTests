
def solve_maze(maze, start, end):
    visited = []
    stack = [start]

    while stack:
        current = stack.pop()

        if current == end:
            return True

        if current in visited:
            continue

        visited.append(current)

        row, col = current

        # Try moving in all four directions
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#':
                stack.append((new_row, new_col))

    return False

# Test the algorithm with a example maze
maze = [
    ['S', '#', '#', '#', 'E'],
    [' ', ' ', ' ', '#', ' '],
    ['#', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

start = (0, 0)
end = (0, 4)

if solve_maze(maze, start, end):
    print("Maze is solvable!")
else:
    print("Maze is not solvable.")
