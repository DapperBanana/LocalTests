
import random

# Initialize crossword grid
grid = [['.' for _ in range(10)] for _ in range(10)]

# Generate list of words
words = ['PYTHON', 'CODE', 'ALGORITHM', 'COMPUTER', 'PROGRAMMING', 'PUZZLE']

# Place words in the grid randomly
for word in words:
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, 9)
            col = random.randint(0, 9 - len(word))
            if all(grid[row][col+i] == '.' or grid[row][col+i] == word[i] for i in range(len(word))):
                for i in range(len(word)):
                    grid[row][col+i] = word[i]
                placed = True
        else:
            row = random.randint(0, 9 - len(word))
            col = random.randint(0, 9)
            if all(grid[row+i][col] == '.' or grid[row+i][col] == word[i] for i in range(len(word))):
                for i in range(len(word)):
                    grid[row+i][col] = word[i]
                placed = True

# Fill in remaining empty spaces with random letters
for i in range(10):
    for j in range(10):
        if grid[i][j] == '.':
            grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Print the crossword puzzle
for row in grid:
    print(" ".join(row))
