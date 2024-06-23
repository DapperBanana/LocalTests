
def print_maze(maze):
    for row in maze:
        print(''.join(row))

def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current == end:
            return True
        visited.add(current)
        for move in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]) and maze[next_pos[0]][next_pos[1]] != '#' and next_pos not in visited:
                stack.append(next_pos)
    return False

maze = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#']
]

start = (1, 1)
end = (3, 4)

print("Maze:")
print_maze(maze)

if solve_maze(maze, start, end):
    print("Path found!")
else:
    print("Path not found")
