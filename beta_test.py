
def solve_maze(maze, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = []
    
    def is_valid_move(move):
        x, y = move
        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
            return False
        if maze[x][y] == "#":
            return False
        if move in visited:
            return False
        return True
    
    def explore_maze(current):
        if current == end:
            return True
        
        visited.append(current)
        
        for direction in directions:
            next_move = (current[0] + direction[0], current[1] + direction[1])
            if is_valid_move(next_move):
                if explore_maze(next_move):
                    return True
                
        return False
    
    if explore_maze(start):
        print("Path found!")
    else:
        print("No path found.")
        

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", "#", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", " ", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]

start = (1, 1)
end = (3, 6)

solve_maze(maze, start, end)
