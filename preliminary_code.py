
import random

def generate_crossword(rows, cols):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Generate random words for horizontal placement
    words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'RANDOM', 'GENERATE']

    for word in words:
        start_row = random.randint(0, rows - 1)
        start_col = random.randint(0, cols - len(word))
        for i, char in enumerate(word):
            grid[start_row][start_col + i] = char

    # Transpose the grid to generate vertical words
    grid_transposed = list(map(list, zip(*grid)))

    for word in words:
        start_col = random.randint(0, cols - 1)
        start_row = random.randint(0, rows - len(word))
        for i, char in enumerate(word):
            grid_transposed[start_col + i][start_row] = char

    grid = list(map(list, zip(*grid_transposed)))

    return grid

def print_crossword(grid):
    for row in grid:
        print(' '.join(row))

rows = 10
cols = 10

crossword_grid = generate_crossword(rows, cols)
print_crossword(crossword_grid)
