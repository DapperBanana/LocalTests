
import random

# Define the grid size
rows = 10
columns = 10

grid = [[' ' for _ in range(columns)] for _ in range(rows)]

# Generate random words for the crossword puzzle
words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'COMPUTER', 'PROGRAMMING']

# Place words in random positions on the grid
for word in words:
    direction = random.choice(['horizontal', 'vertical'])
    if direction == 'horizontal':
        row = random.randint(0, rows - 1)
        col = random.randint(0, columns - len(word))
        for i, letter in enumerate(word):
            grid[row][col + i] = letter
    else:
        row = random.randint(0, rows - len(word))
        col = random.randint(0, columns - 1)
        for i, letter in enumerate(word):
            grid[row + i][col] = letter

# Fill in remaining empty spaces with random letters
for i in range(rows):
    for j in range(columns):
        if grid[i][j] == ' ':
            grid[i][j] = chr(random.randint(65, 90))

# Print the crossword puzzle grid
for row in grid:
    print(' '.join(row))
