
import random

# Set the size of the crossword puzzle
rows = 10
cols = 10

# Create an empty crossword grid
grid = [[' ' for _ in range(cols)] for _ in range(rows)]

# List of words to fill in the puzzle
words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'RANDOM', 'GENERATE', 'PROGRAM']

# Place words randomly in the crossword grid
for word in words:
    direction = random.choice(['H', 'V'])
    if direction == 'H':
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - len(word))
        for i in range(len(word)):
            grid[row][col+i] = word[i]
    else:
        row = random.randint(0, rows - len(word))
        col = random.randint(0, cols - 1)
        for i in range(len(word)):
            grid[row+i][col] = word[i]

# Print the crossword puzzle
print("Random Crossword Puzzle:")
for row in grid:
    print(' '.join(row))
