
import random
import string

# Generate a 10x10 crossword grid
grid = [[' ' for _ in range(10)] for _ in range(10)]

# Generate a list of words to place in the crossword
words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'RANDOM', 'GENERATE', 'PROGRAM']

# Fill in the grid with random words
for word in words:
    direction = random.choice(['horizontal', 'vertical'])
    if direction == 'horizontal':
        row = random.randint(0, 9)
        col = random.randint(0, 10 - len(word))
        for i in range(len(word)):
            grid[row][col+i] = word[i]
    else:
        row = random.randint(0, 10 - len(word))
        col = random.randint(0, 9)
        for i in range(len(word)):
            grid[row+i][col] = word[i]

# Print the crossword grid
for row in grid:
    print(' '.join(row))

# Print the list of words to find
print('\nWords to find:')
for word in words:
    print(word)
