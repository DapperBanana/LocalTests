
import random

# Maze class
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[0 for _ in range(width)] for _ in range(height)]
    
    def generate(self):
        stack = [(0, 0)]
        visited = set()
        
        while stack:
            current_cell = stack[-1]
            visited.add(current_cell)
            neighbors = []
            
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_cell = (current_cell[0] + dx, current_cell[1] + dy)
                if 0 <= next_cell[0] < self.width and 0 <= next_cell[1] < self.height and next_cell not in visited:
                    neighbors.append(next_cell)
            
            if neighbors:
                next_cell = random.choice(neighbors)
                wall = ((current_cell[0] + next_cell[0]) // 2, (current_cell[1] + next_cell[1]) // 2)
                self.maze[wall[1]][wall[0]] = 1
                stack.append(next_cell)
            else:
                stack.pop()
    
    def print(self):
        for row in self.maze:
            print(' '.join(['#' if cell else '.' for cell in row]))
    
    def solve(self):
        start = (0, 0)
        end = (self.width - 1, self.height - 1)
        open_set = {start}
        came_from = {}
        
        g_score = {start: 0}
        f_score = {start: abs(start[0] - end[0]) + abs(start[1] - end[1])}
        
        while open_set:
            current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
            
            if current == end:
                path = []
                while current in came_from:
                    path.insert(0, current)
                    current = came_from[current]
                return [start] + path + [end]
            
            open_set.remove(current)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height and not self.maze[neighbor[1]][neighbor[0]]:
                    tentative_g_score = g_score[current] + 1
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                        open_set.add(neighbor)
        
        return None

# Generate random maze
maze = Maze(10, 10)
maze.generate()
maze.print()

# Find and print solution
solution = maze.solve()
if solution:
    print("Solution:")
    for cell in solution:
        x, y = cell
        maze.maze[y][x] = 2
    maze.print()
else:
    print("No solution found.")
