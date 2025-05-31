
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        if current == end:
            return True
        
        if current in visited:
            continue
        
        visited.add(current)
        
        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            nrow, ncol = neighbor
            if 0 <= nrow < len(maze) and 0 <= ncol < len(maze[0]) and maze[nrow][ncol] != "#":
                stack.append(neighbor)
    
    return False

# Sample maze with '#' as walls and 'S' as start and 'E' as end
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['S', ' ', '#', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', '#', ' ', ' ', ' '],
    ['#', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', 'E', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

start = (1, 0)
end = (4, 5)

if solve_maze(maze, start, end):
    print("Maze solved!")
else:
    print("No solution found.")
