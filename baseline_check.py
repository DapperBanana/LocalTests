
maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze):
    for row in maze:
        print("".join(row))

def solve_maze(maze, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(curr):
        if curr == end:
            return True
        
        x, y = curr
        maze[x][y] = "x"
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == " ":
                if dfs((nx, ny)):
                    return True
        
        maze[x][y] = " "
        return False
    
    return dfs(start)

start = (1, 1)
end = (3, 5)

print("Original maze:")
print_maze(maze)

if solve_maze(maze, start, end):
    print("\nSolved maze:")
    print_maze(maze)
else:
    print("\nNo solution found.")
