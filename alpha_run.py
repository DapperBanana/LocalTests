
import random

# Constants
WALL = '#'
EMPTY = ' '
START = 'S'
GOAL = 'G'
PATH = '.'

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[WALL for _ in range(width)] for _ in range(height)]
        self.start = (1, 1)
        self.goal = (width - 2, height - 2)
        self.generate()

    def generate(self):
        stack = [(1, 1)]
        while stack:
            x, y = stack[-1]
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            random.shuffle(neighbors)
            found = False
            for nx, ny in neighbors:
                if 0 < nx < self.width - 1 and 0 < ny < self.height - 1 and self.maze[ny][nx] == WALL:
                    self.maze[ny][nx] = EMPTY
                    self.maze[y + (ny - y) // 2][x + (nx - x) // 2] = EMPTY
                    stack.append((nx, ny))
                    found = True
                    break
            if not found:
                stack.pop()

        self.maze[self.start[1]][self.start[0]] = START
        self.maze[self.goal[1]][self.goal[0]] = GOAL

    def solve(self):
        open_set = [(self.start, 0, 0)]
        closed_set = set()
        came_from = {}
        while open_set:
            current, g_score, _ = min(open_set, key=lambda x: x[1])
            open_set.remove((current, g_score, 0))
            closed_set.add(current)

            if current == self.goal:
                path = []
                while current in came_from:
                    path.insert(0, current)
                    current = came_from[current]
                for x, y in path:
                    self.maze[y][x] = PATH
                break

            x, y = current
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < self.width - 1 and 0 < ny < self.height - 1 and self.maze[ny][nx] != WALL and (nx, ny) not in closed_set]
            for nx, ny in neighbors:
                if (nx, ny) not in [node for node, _, _ in open_set]:
                    g = g_score + 1
                    h = abs(self.goal[0] - nx) + abs(self.goal[1] - ny)
                    open_set.append(((nx, ny), g, h))
                    came_from[(nx, ny)] = current

    def display(self):
        for row in self.maze:
            print(' '.join(row))

maze = Maze(21, 21)
maze.solve()
maze.display()
