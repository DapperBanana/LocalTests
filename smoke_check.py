
import random

# Define the size of the crossword grid
rows = 10
cols = 10

# Generate a random grid with letters and empty squares
grid = [[' ' for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if random.random() < 0.3:  # Fill 30% of the grid with random letters
            grid[i][j] = chr(random.randint(65, 90))  # Random uppercase letter

# Print the crossword grid
print("Random Crossword Puzzle:")
for row in grid:
    print(''.join(row))
