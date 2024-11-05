
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', 'E', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

def solve(maze, position):
    if maze[position[0]][position[1]] == 'E':
        print("Maze solved!")
        return True
    elif maze[position[0]][position[1]] == '#' or maze[position[0]][position[1]] == 'X':
        return False
    
    maze[position[0]][position[1]] = 'X'
    
    # Try moving up
    if solve(maze, (position[0]-1, position[1])):
        print(f"({position[0]}, {position[1]}) -> Up")
        return True
    # Try moving right
    if solve(maze, (position[0], position[1]+1)):
        print(f"({position[0]}, {position[1]}) -> Right")
        return True
    # Try moving down
    if solve(maze, (position[0]+1, position[1])):
        print(f"({position[0]}, {position[1]}) -> Down")
        return True
    # Try moving left
    if solve(maze, (position[0], position[1]-1)):
        print(f"({position[0]}, {position[1]}) -> Left")
        return True
    
    return False

start_position = (6, 1)
solve(maze, start_position)
