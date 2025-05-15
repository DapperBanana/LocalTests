
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
        
        x, y = current
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
                stack.append((new_x, new_y))
    
    return False

maze = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#'],
]

start = (1, 1)
end = (3, 4)

if solve_maze(maze, start, end):
    print("The maze has a solution.")
else:
    print("The maze does not have a solution.")
