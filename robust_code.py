
import random

# Define the crossword puzzle grid size
rows = 10
columns = 10
grid = [[' ' for _ in range(columns)] for _ in range(rows)]

# Generate some random words to place in the crossword puzzle
words = ["CAT", "DOG", "BIRD", "FISH", "LION", "TIGER", "ZEBRA", "ELEPHANT"]
random.shuffle(words)

# Place the words in the puzzle grid horizontally and vertically
for word in words:
    direction = random.choice(['horizontal', 'vertical'])
    if direction == 'horizontal':
        row = random.randint(0, rows - 1)
        col = random.randint(0, columns - len(word))
        for i in range(len(word)):
            grid[row][col + i] = word[i]
    else:
        row = random.randint(0, rows - len(word))
        col = random.randint(0, columns - 1)
        for i in range(len(word)):
            grid[row + i][col] = word[i]

# Print the crossword puzzle
for row in grid:
    print(' '.join(row))
