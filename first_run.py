
class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.num_rows = len(maze)
        self.num_cols = len(maze[0])
        self.visited = [[False for _ in range(self.num_cols)] for _ in range(self.num_rows)]
    
    def solve_maze(self, start_row, start_col):
        if self._is_valid_move(start_row, start_col):
            self.visited[start_row][start_col] = True
            
            if self.maze[start_row][start_col] == 'G':
                return True
            
            if self.solve_maze(start_row+1, start_col) or self.solve_maze(start_row-1, start_col) or self.solve_maze(start_row, start_col+1) or self.solve_maze(start_row, start_col-1):
                return True
            
            self.visited[start_row][start_col] = False
        
        return False
    
    def _is_valid_move(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols and not self.visited[row][col] and self.maze[row][col] != '#'

maze = [
    ['S', '#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '#', '.', '#'],
    ['#', '#', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#', 'G']
]

solver = MazeSolver(maze)
if solver.solve_maze(0, 0):
    print("The maze has a solution!")
else:
    print("No solution found for the maze.")
