
def solve_maze(maze, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def is_valid(x, y):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
            return False
        if maze[x][y] == 'X':
            return False
        return True

    def dfs(x, y):
        if x == end[0] and y == end[1]:
            return True
        maze[x][y] = 'X'  # mark as visited
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                if dfs(new_x, new_y):
                    return True
                
        return False

    if dfs(start[0], start[1]):
        print("Path found!")
    else:
        print("No path found.")

# Example maze (1 represents walls, 0 represents paths)
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

start = (1, 1)
end = (3, 3)

solve_maze(maze, start, end)
