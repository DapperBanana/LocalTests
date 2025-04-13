
import random

# Generate a random maze
def generate_maze(size):
    maze = [["#" for _ in range(size)] for _ in range(size)]
    stack = [(0, 0)]
    while stack:
        x, y = stack[-1]
        maze[y][x] = "."
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbors)
        for nx, ny in neighbors:
            if 0 <= nx < size and 0 <= ny < size and maze[ny][nx] == "#":
                maze[ny][nx] = "."
                stack.append((nx, ny))
                stack.append((x + (nx-x)//2, y + (ny-y)//2))
                break
        else:
            stack.pop()
    return maze

# Find the solution to the maze
def find_solution(maze, size):
    start = (0, 0)
    end = (size-1, size-1)
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and maze[ny][nx] == "." and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

# Main function
if __name__ == "__main__":
    size = 10
    maze = generate_maze(size)
    for row in maze:
        print(" ".join(row))
    
    solution = find_solution(maze, size)
    print("\nSolution:")
    for x, y in solution:
        maze[y][x] = "X"
    
    for row in maze:
        print(" ".join(row))
