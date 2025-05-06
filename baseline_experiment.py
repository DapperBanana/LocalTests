
maze = [
    "##########",
    "#   #    #",
    "# # # ## #",
    "# #   ## #",
    "# ## ##  #",
    "#    ##  #",
    "##########"
]

def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    def dfs(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or maze[row][col] in ['#', 'X']:
            return False
        
        if maze[row][col] == 'E':
            return True
        
        maze[row] = maze[row][:col] + 'X' + maze[row][col+1:]

        if dfs(row+1, col) or dfs(row-1, col) or dfs(row, col+1) or dfs(row, col-1):
            return True
        
        maze[row] = maze[row][:col] + ' ' + maze[row][col+1:]
        return False

    start_row, start_col = start
    end_row, end_col = end

    maze[start_row] = maze[start_row][:start_col] + 'S' + maze[start_row][start_col+1:]
    maze[end_row] = maze[end_row][:end_col] + 'E' + maze[end_row][end_col+1:]

    if dfs(start_row, start_col):
        for row in maze:
            print(row)
    else:
        print("No path exists")

start = (1, 1)
end = (5, 1)
solve_maze(maze, start, end)
