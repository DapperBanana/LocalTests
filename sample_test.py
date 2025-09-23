
import random

# Function to generate a random maze using Depth First Search algorithm
def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]

    visited = set()
    stack = [(0, 0)]

    while stack:
        current = stack[-1]
        visited.add(current)
        maze[current[0]][current[1]] = ' '

        neighbors = [(current[0]-2, current[1]), (current[0]+2, current[1),
                     (current[0], current[1]-2), (current[0], current[1]+2)]
        random.shuffle(neighbors)

        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in visited]

        if unvisited_neighbors:
            next_cell = unvisited_neighbors[0]
            stack.append(next_cell)
            maze[(current[0] + next_cell[0])//2][(current[1] + next_cell[1])//2] = ' '
        else:
            stack.pop()

    return maze

# Function to find the solution to the maze using Breadth First Search algorithm
def solve_maze(maze, start, end):
    queue = [start]
    parents = {start: None}

    while queue:
        current = queue.pop(0)

        if current == end:
            path = []
            while current:
                path.insert(0, current)
                current = parents[current]
            return path

        for neighbor in [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]:
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == ' ' and neighbor not in parents:
                queue.append(neighbor)
                parents[neighbor] = current

    return None

# Main function to generate and solve a random maze
def main():
    rows = 11
    cols = 21

    maze = generate_maze(rows, cols)

    start = (0, 0)
    end = (rows-1, cols-1)

    path = solve_maze(maze, start, end)

    if path:
        for i in range(rows):
            print(''.join(maze[i]))

        print('\nPath to solve the maze:')
        for cell in path:
            maze[cell[0]][cell[1]] = 'X'

        for i in range(rows):
            print(''.join(maze[i]))
    else:
        print('No solution found for the maze!')

if __name__ == '__main__':
    main()
