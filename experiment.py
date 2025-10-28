
def solve_maze(maze, start, end):
    queue = [start]
    visited = [start]
    parent = {}
    
    while queue:
        current = queue.pop(0)
        
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == " " and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.append((new_row, new_col))
                parent[(new_row, new_col)] = current
    
    return None

maze = [
    ["#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#"]
]

start = (1, 1)
end = (3, 3)

path = solve_maze(maze, start, end)

if path:
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) in path:
                print("*", end="")
            else:
                print(maze[row][col], end="")
        print()
else:
    print("No path found!")
