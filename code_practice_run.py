
def solve_maze(maze, start, end):
    stack = [(start, [start])]
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == end:
            return path
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#' and (nx, ny) not in path:
                stack.append(((nx, ny), path + [(nx, ny)])
    return None

# Define the maze as a 2D list
maze = [
    list("##########"),
    list("#S   #   #"),
    list("#    # # #"),
    list("#  # #   #"),
    list("#    #   #"),
    list("# # #    #"),
    list("# #      #"),
    list("######## #"),
    list("#   #    #"),
    list("#   #    #"),
    list("#   #    #"),
    list("#      E#"),
    list("##########")
]

start = (1, 1)  # Starting position
end = (11, 9)  # Ending position

path = solve_maze(maze, start, end)

if path:
    for x, y in path:
        maze[x][y] = 'X'
    for row in maze:
        print(''.join(row))
else:
    print("No path found!")
