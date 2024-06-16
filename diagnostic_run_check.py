
import random

# Create a list of words to use in the crossword puzzle
words = ['python', 'programming', 'language', 'computer', 'code', 'variable', 'function', 'algorithm']

# Create a list to store the crossword puzzle grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Randomly place the words in the grid
for word in words:
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, 9)
            col = random.randint(0, 9 - len(word))
            if all(grid[row][col+i] == ' ' or grid[row][col+i] == word[i] for i in range(len(word))):
                for i in range(len(word)):
                    grid[row][col+i] = word[i]
                placed = True
        else:
            row = random.randint(0, 9 - len(word))
            col = random.randint(0, 9)
            if all(grid[row+i][col] == ' ' or grid[row+i][col] == word[i] for i in range(len(word))):
                for i in range(len(word)):
                    grid[row+i][col] = word[i]
                placed = True

# Print the crossword puzzle grid
for row in grid:
    print(' '.join(row))
