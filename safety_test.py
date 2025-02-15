
def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        current_pos = stack.pop()
        if current_pos == end:
            return True
        
        visited.add(current_pos)
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for move in moves:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            if (0 <= new_pos[0] < len(maze)) and (0 <= new_pos[1] < len(maze[0])) and maze[new_pos[0]][new_pos[1]] != '#' and new_pos not in visited:
                stack.append(new_pos)
    
    return False

maze = [
    ['#', 'S', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', 'E', '#'],
    ['#', '#', '#', '#', '#', '#'],
]

start = (0, 1)
end = (4, 4)

if solve_maze(maze, start, end):
    print("Maze solved!")
else:
    print("Maze cannot be solved.")
