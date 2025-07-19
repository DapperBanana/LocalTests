
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    
    while stack:
        current_cell = stack.pop()
        
        if current_cell == end:
            return True
        
        if current_cell in visited:
            continue
        
        visited.add(current_cell)
        
        row, col = current_cell
        
        if row > 0 and maze[row-1][col] != '#':
            stack.append((row-1, col))
        if row < len(maze) - 1 and maze[row+1][col] != '#':
            stack.append((row+1, col))
        if col > 0 and maze[row][col-1] != '#':
            stack.append((row, col-1))
        if col < len(maze[0]) - 1 and maze[row][col+1] != '#':
            stack.append((row, col+1))
    
    return False

# Example maze
maze = [
    ['S', '#', '#', '#', '#'],
    [' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    [' ', ' ', ' ', ' ', ' '],
    ['#', '#', ' ', '#', 'E']
]

start = (0, 0)
end = (4, 4)

if solve_maze(maze, start, end):
    print("Maze solved!")
else:
    print("No solution found.")
