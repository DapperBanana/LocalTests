
import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    def generate_random_maze(self):
        def recursive_backtracking(row, col):
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                new_row, new_col = row + dx * 2, col + dy * 2
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] == ' ':
                    self.grid[row + dx][col + dy] = ' '
                    self.grid[row + dx * 2][col + dy * 2] = ' '
                    recursive_backtracking(row + dx * 2, col + dy * 2)
        
        start_row, start_col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        self.grid[start_row][start_col] = ' '
        recursive_backtracking(start_row, start_col)
    
    def print_maze(self):
        for row in self.grid:
            print(''.join(row))
    
    def find_solution(self):
        def heuristic(row, col):
            return abs(row - self.rows // 2) + abs(col - self.cols // 2)
        
        open_list = [(0, heuristic(0, 0), 0, 0)]
        closed_list = set()
        while open_list:
            _, _, row, col = min(open_list)
            if row == self.rows - 1 and col == self.cols - 1:
                return
            open_list.remove((_, _, row, col))
            closed_list.add((row, col))
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] == ' ' and (new_row, new_col) not in closed_list:
                    open_list.append((heuristic(new_row, new_col), heuristic(new_row, new_col), new_row, new_col))
    
        print("No solution found")

# Generate a random maze
maze = Maze(10, 20)
maze.generate_random_maze()
maze.print_maze()

# Find the solution for the maze
print("\nFinding solution for the maze:")
maze.find_solution()
