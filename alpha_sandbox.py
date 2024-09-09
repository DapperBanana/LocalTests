
import random

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]
    visited[0][0] = True

    while stack:
        current_cell = stack[-1]
        x, y = current_cell

        # Get unvisited neighbors
        neighbors = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
        random.shuffle(neighbors)
        
        found = False
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                found = True
                maze[(nx + x) // 2][(ny + y) // 2] = ' '
                visited[nx][ny] = True
                stack.append((nx, ny))
                break

        if not found:
            stack.pop()

    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]

    while stack:
        x, y = stack[-1]

        if x == rows - 1 and y == cols - 1:
            break
        
        found = False
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == ' ' and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
                found = True
                break

        if not found:
            stack.pop()
    
    return stack

# Main function
if __name__ == "__main__":
    rows, cols = 10, 10
    maze = generate_maze(rows, cols)

    print("Random Maze:")
    for row in maze:
        print("".join(row))

    solution = solve_maze(maze)

    if (solution):
        print("\nSolution Path:")
        for x, y in solution:
            maze[x][y] = 'X'
        
        for row in maze:
            print("".join(row))
    else:
        print("\nNo solution found.")
