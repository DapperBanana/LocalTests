
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) == end:
            print("Path found!")
            return True
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        if x > 0 and maze[x-1][y] != '#':
            stack.append((x-1, y))
        if x < len(maze)-1 and maze[x+1][y] != '#':
            stack.append((x+1, y))
        if y > 0 and maze[x][y-1] != '#':
            stack.append((x, y-1))
        if y < len(maze[0])-1 and maze[x][y+1] != '#':
            stack.append((x, y+1))
    
    print("No path found")
    return False

# Example maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

start = (1, 1)
end = (4, 6)

solve_maze(maze, start, end)
