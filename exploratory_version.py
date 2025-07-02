
import random
from collections import deque

# Class to represent a cell in the maze
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.visited = False

# Function to generate a random maze
def generate_maze(rows, cols):
    maze = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
    stack = [(0, 0)]
    maze[0][0].visited = True

    while stack:
        current_row, current_col = stack[-1]
        neighbors = []

        if current_row > 0 and not maze[current_row - 1][current_col].visited:
            neighbors.append((current_row - 1, current_col))
        if current_col < cols - 1 and not maze[current_row][current_col + 1].visited:
            neighbors.append((current_row, current_col + 1))
        if current_row < rows - 1 and not maze[current_row + 1][current_col].visited:
            neighbors.append((current_row + 1, current_col))
        if current_col > 0 and not maze[current_row][current_col - 1].visited:
            neighbors.append((current_row, current_col - 1))

        if neighbors:
            next_row, next_col = random.choice(neighbors)

            maze[current_row][current_col].walls[f'{next_row - current_row}{next_col - current_col}'] = False
            maze[next_row][next_col].walls[f'{current_row - next_row}{current_col - next_col}'] = False

            maze[next_row][next_col].visited = True
            stack.append((next_row, next_col))
        else:
            stack.pop()

    return maze

# Function to find the solution of the maze using breadth-first search
def find_solution(maze, rows, cols):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        current_row, current_col, path = queue.popleft()

        if current_row == rows - 1 and current_col == cols - 1:
            return path

        visited.add((current_row, current_col))

        for direction, (offset_row, offset_col) in {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}.items():
            new_row, new_col = current_row + offset_row, current_col + offset_col

            if 0 <= new_row < rows and 0 <= new_col < cols and not maze[current_row][current_col].walls[direction] and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, path + [direction]))

    return None

# Main program
rows = 5
cols = 5

maze = generate_maze(rows, cols)
solution = find_solution(maze, rows, cols)

# Print maze
for row in maze:
    for cell in row:
        print('+', end='')
        if cell.walls['N']:
            print('-', end='')
        else:
            print(' ', end='')
    print('+')

    for cell in row:
        if cell.walls['W']:
            print('|', end='')
        else:
            print(' ', end='')
        print(' ', end='')
    if row[-1].walls['E']:
        print('|')
    else:
        print(' ')

print('+-' * cols + '+')

# Print solution
if solution:
    print('Solution:', ''.join(solution))
else:
    print('No solution found')
