
import random
import heapq

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            maze[i][j] = ' '
    stack = [(0, 0)]
    while stack:
        current_cell = stack[-1]
        neighbors = []
        if current_cell[0] >= 2 and maze[current_cell[0]-2][current_cell[1]] == '#':
            neighbors.append((current_cell[0]-2, current_cell[1]))
        if current_cell[0] < rows - 2 and maze[current_cell[0]+2][current_cell[1]] == '#':
            neighbors.append((current_cell[0]+2, current_cell[1]))
        if current_cell[1] >= 2 and maze[current_cell[0]][current_cell[1]-2] == '#':
            neighbors.append((current_cell[0], current_cell[1]-2))
        if current_cell[1] < cols - 2 and maze[current_cell[0]][current_cell[1]+2] == '#':
            neighbors.append((current_cell[0], current_cell[1]+2))
        
        if neighbors:
            next_cell = random.choice(neighbors)
            maze[next_cell[0]][next_cell[1]] = ' '
            maze[(current_cell[0]+next_cell[0])//2][(current_cell[1]+next_cell[1])//2] = ' '
            stack.append(next_cell)
        else:
            stack.pop()
    
    return maze

def find_path(maze):
    start = (0, 0)
    end = (len(maze)-1, len(maze[0])-1)
    open_list = [(0, start)]
    closed_list = set()
    parent = {}
    g_score = {start: 0}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == end:
            path = []
            while current in parent:
                path.insert(0, current)
                current = parent[current]
            path.insert(0, start)
            return path
        
        closed_list.add(current)
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_cell = (current[0]+i, current[1]+j)
            if 0 <= next_cell[0] < len(maze) and 0 <= next_cell[1] < len(maze[0]) and maze[next_cell[0]][next_cell[1]] == ' ' and next_cell not in closed_list:
                tentative_g_score = g_score[current] + 1
                if next_cell not in g_score or tentative_g_score < g_score[next_cell]:
                    g_score[next_cell] = tentative_g_score
                    f_score = tentative_g_score + abs(next_cell[0] - end[0]) + abs(next_cell[1] - end[1])
                    heapq.heappush(open_list, (f_score, next_cell))
                    parent[next_cell] = current
    
    return None

rows = 10
cols = 10
maze = generate_maze(rows, cols)
for row in maze:
    print(''.join(row))
    
path = find_path(maze)
if path:
    for cell in path:
        maze[cell[0]][cell[1]] = '*'
    print('\nSolution:')
    for row in maze:
        print(''.join(row))
else:
    print('\nNo solution found.')
