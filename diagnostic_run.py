
import random

# Generate a random maze
def generate_maze(rows, cols):
    maze = [["#" for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]
    visited = set([(0, 0])

    while stack:
        current_cell = stack[-1]
        x, y = current_cell

        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            next_cell = random.choice(neighbors)
            nx, ny = next_cell
            maze[nx][ny] = " "
            stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()

    maze[0][0] = "S"
    maze[rows-1][cols-1] = "E"

    return maze

# Solve the maze using depth-first search
def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    stack = [(0, 0)]
    visited = set([(0, 0)])
    path = []
    
    while stack:
        x, y = stack[-1]

        if maze[x][y] == "E":
            break

        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != "#" and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            next_cell = neighbors[0]
            stack.append(next_cell)
            visited.add(next_cell)
            path.append(next_cell)
        else:
            stack.pop()

    for x, y in path:
        maze[x][y] = "."

    return maze

# Main function
if __name__ == "__main__":
    rows, cols = 10, 10  # Size of the maze
    maze = generate_maze(rows, cols)
    
    print("Random maze:")
    for row in maze:
        print("".join(row))

    solved_maze = solve_maze(maze)
    print("\nSolved maze:")
    for row in solved_maze:
        print("".join(row))
