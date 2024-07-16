
import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    for i in range(1, height, 2):
        for j in range(1, width, 2):
            maze[i][j] = ' '
    
    stack = [(1, 1)]
    while stack:
        current_cell = stack[-1]
        x, y = current_cell
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbors)
        
        found_new_cell = False
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                stack.append(neighbor)
                maze[ny][nx] = ' '
                maze[y + (ny - y) // 2][x + (nx - x) // 2] = ' '
                found_new_cell = True
                break
        
        if not found_new_cell:
            stack.pop()
    
    return maze

def dfs(maze, x, y, visited):
    if maze[y][x] == ' ':
        visited.add((x, y))
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if (nx, ny) not in visited:
                if dfs(maze, nx, ny, visited):
                    return True
        return False
    elif maze[y][x] == 'F':
        return True
    else:
        return False

def solve_maze(maze):
    start_x, start_y = 1, 1
    end_x, end_y = len(maze[0])-2, len(maze)-2
    maze[start_y][start_x] = 'S'
    maze[end_y][end_x] = 'F'
    
    visited = set()
    dfs(maze, start_x, start_y, visited)
    
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    width, height = 21, 21
    maze = generate_maze(width, height)
    solved_maze = solve_maze(maze)
    
    print("Random Maze:")
    print_maze(maze)
    
    print("\nSolved Maze:")
    print_maze(solved_maze)
