
import random

# Constants for maze dimensions
WIDTH = 20
HEIGHT = 20

def generate_maze():
    maze = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    stack = [(0, 0)]
    
    while stack:
        current_cell = stack[-1]
        maze[current_cell[1]][current_cell[0]] = ' '
        
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = current_cell[0] + dx, current_cell[1] + dy
            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and maze[new_y][new_x] == '#':
                count = 0
                for dx2, dy2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    adj_x, adj_y = new_x + dx2, new_y + dy2
                    if 0 <= adj_x < WIDTH and 0 <= adj_y < HEIGHT and maze[adj_y][adj_x] == ' ':
                        count += 1
                if count == 1:
                    neighbors.append((new_x, new_y))
                
        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
        else:
            stack.pop()

    return maze

def solve_maze(maze):
    stack = [(0, 0)]
    visited = set()
    
    while stack:
        current_cell = stack[-1]
        if current_cell == (WIDTH - 1, HEIGHT - 1):
            break
        
        visited.add(current_cell)
        
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = current_cell[0] + dx, current_cell[1] + dy
            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and maze[new_y][new_x] == ' ' and (new_x, new_y) not in visited:
                neighbors.append((new_x, new_y))
                
        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
        else:
            stack.pop()
    
    # Mark the path in the maze
    for cell in stack:
        maze[cell[1]][cell[0]] = '.'
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == '__main__':
    maze = generate_maze()
    
    print("Generated maze:")
    print_maze(maze)
    
    solved_maze = solve_maze(maze)
    
    print("\nSolved maze:")
    print_maze(solved_maze)
