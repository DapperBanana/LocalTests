
import random

# Function to generate a random maze using Prim's algorithm
def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]
    visited = set()
    stack = [(random.randint(0, width-1), random.randint(0, height-1))]
    visited.add(stack[-1])

    while stack:
        x, y = stack[-1]
        neighbors = []

        if x > 1 and (x-2, y) not in visited:
            neighbors.append((x-2, y))
        if y > 1 and (x, y-2) not in visited:
            neighbors.append((x, y-2))
        if x < width-2 and (x+2, y) not in visited:
            neighbors.append((x+2, y))
        if y < height-2 and (x, y+2) not in visited:
            neighbors.append((x, y+2))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(y+ny)//2][(x+nx)//2] = " "
            maze[ny][nx] = " "
            stack.append((nx, ny))
            visited.add((nx, ny))
        else:
            stack.pop()

    maze[0][0] = " "
    maze[height-1][width-1] = " "
    
    return maze

# Function to solve the maze using depth-first search
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        x, y = stack[-1]
        
        if (x, y) == end:
            return True
        
        visited.add((x, y))

        neighbors = []

        if x > 0 and maze[y][x-1] != "#" and (x-1, y) not in visited:
            neighbors.append((x-1, y))
        if y > 0 and maze[y-1][x] != "#" and (x, y-1) not in visited:
            neighbors.append((x, y-1))
        if x < len(maze[0])-1 and maze[y][x+1] != "#" and (x+1, y) not in visited:
            neighbors.append((x+1, y))
        if y < len(maze)-1 and maze[y+1][x] != "#" and (x, y+1) not in visited:
            neighbors.append((x, y+1))

        if neighbors:
            nx, ny = neighbors.pop()
            stack.append((nx, ny))
        else:
            stack.pop()
    
    return False

def print_maze(maze):
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    width = 15
    height = 15
    maze = generate_maze(width, height)
    start = (0, 0)
    end = (width-1, height-1)

    print("Generated maze:")
    print_maze(maze)

    if solve_maze(maze, start, end):
        print("\nMaze solved!")
    else:
        print("\nNo solution found!")
