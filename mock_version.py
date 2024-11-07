
def solve_maze(maze, start, end):
    paths = [[start]]
    visited = set()
    
    while paths:
        path = paths.pop(0)
        current_position = path[-1]
        
        if current_position == end:
            return path
        
        if current_position in visited:
            continue
        visited.add(current_position)
        
        (x, y) = current_position
        directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        for new_position in directions:
            (new_x, new_y) = new_position
            
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0:
                new_path = list(path)
                new_path.append(new_position)
                paths.append(new_path)
    
    return None

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

solution = solve_maze(maze, start, end)

if solution:
    print("Path found:")
    for step in solution:
        print(step)
else:
    print("No path found")
