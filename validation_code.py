
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()

    def solve_maze(self, start, end):
        if start == end:
            return [start]
        
        self.visited.add(start)
        
        for next_move in [(start[0]+1, start[1]), (start[0]-1, start[1]), (start[0], start[1]+1), (start[0], start[1]-1)]:
            if next_move not in self.visited and self.maze[next_move[0]][next_move[1]] != '#':
                path = self.solve_maze(next_move, end)
                if path:
                    return [start] + path
        
        return None

# Define the maze as a list of lists
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', 'E'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

solver = MazeSolver(maze)
start = (1, 1)
end = (7, 9)
solution = solver.solve_maze(start, end)

if solution:
    for step in solution:
        maze[step[0]][step[1]] = '*'
    
    for row in maze:
        print(''.join(row))
else:
    print("No solution found.")
