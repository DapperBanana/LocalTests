
import random

# Generate a random maze
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    stack = [(0, 0)]
    while stack:
        current_cell = stack[-1]
        maze[current_cell[0]][current_cell[1]] = ' '
        
        neighbors = []
        for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            r, c = current_cell[0] + dr, current_cell[1] + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == '#':
                neighbors.append((r, c))
        
        if neighbors:
            next_cell = random.choice(neighbors)
            maze[(current_cell[0] + next_cell[0]) // 2][(current_cell[1] + next_cell[1]) // 2] = ' '
            stack.append(next_cell)
        else:
            stack.pop()
    
    return maze

# Solve the maze using depth-first search
def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or maze[r][c] == '#' or visited[r][c]:
            return False
        if (r, c) == end:
            return True
        
        visited[r][c] = True
        if dfs(r + 1, c) or dfs(r - 1, c) or dfs(r, c + 1) or dfs(r, c - 1):
            return True
        
        return False
    
    dfs(start[0], start[1])
    
    return visited

# Main function
if __name__ == "__main__":
    rows, cols = 10, 10
    maze = generate_maze(rows, cols)
    start, end = (0, 0), (rows-1, cols-1)
    
    print("Generated Maze:")
    for row in maze:
        print(''.join(row))
    
    solution = solve_maze(maze, start, end)
    
    print("\nSolution:")
    for r in range(rows):
        for c in range(cols):
            if solution[r][c]:
                maze[r][c] = '+'
    for row in maze:
        print(''.join(row))
