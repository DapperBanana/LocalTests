
import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    stack = [(0, 0)]
    visited = set()
    while stack:
        current_cell = stack[-1]
        maze[current_cell[1]][current_cell[0]] = '.'
        visited.add(current_cell)

        unvisited_neighbors = [(x, y) for x, y in [(current_cell[0]+2, current_cell[1]), (current_cell[0]-2, current_cell[1]), (current_cell[0], current_cell[1]+2), (current_cell[0], current_cell[1]-2)] if 0 <= x < width and 0 <= y < height and (x, y) not in visited]
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            stack.append(next_cell)
            maze[(current_cell[1]+next_cell[1])//2][(current_cell[0]+next_cell[0])//2] = '.'
        else:
            stack.pop()
    
    return maze

def find_solution(maze, start, goal):
    def heuristic(node):
        return abs(node[0]-goal[0]) + abs(node[1]-goal[1])
    
    open_list = [(start, 0, heuristic(start))]
    closed_list = set()
    
    while open_list:
        current_node, g_cost, h_cost = min(open_list, key=lambda x: x[1]+x[2])
        if current_node == goal:
            return True
        
        open_list.remove((current_node, g_cost, h_cost))
        closed_list.add(current_node)
        
        neighbors = [(current_node[0]+1, current_node[1]), (current_node[0]-1, current_node[1]), (current_node[0], current_node[1]+1), (current_node[0], current_node[1]-1)]
        for neighbor in neighbors:
            if 0 <= neighbor[0] < len(maze[0]) and 0 <= neighbor[1] < len(maze) and maze[neighbor[1]][neighbor[0]] != '#' and neighbor not in closed_list:
                open_list.append((neighbor, g_cost+1, heuristic(neighbor)))
    
    return False

width, height = 10, 10
maze = generate_maze(width, height)

start = (0, 0)
goal = (width-1, height-1)

if find_solution(maze, start, goal):
    print("Maze solution found!")
else:
    print("No solution found")
