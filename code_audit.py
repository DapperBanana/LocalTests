
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]

def solve_maze(maze):
    start_pos = (0, 0)
    end_pos = (len(maze)-1, len(maze[0])-1)
    stack = [start_pos]
    visited = set()

    while stack:
        curr_pos = stack.pop()
        if curr_pos == end_pos:
            return True

        visited.add(curr_pos)
        neighbors = get_neighbors(maze, curr_pos)

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return False

def get_neighbors(maze, curr_pos):
    neighbors = []
    row, col = curr_pos

    if row > 0 and maze[row-1][col] == 0:
        neighbors.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] == 0:
        neighbors.append((row+1, col))
    if col > 0 and maze[row][col-1] == 0:
        neighbors.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] == 0:
        neighbors.append((row, col+1))

    return neighbors

if solve_maze(maze):
    print("Maze solved!")
else:
    print("No solution found!")
