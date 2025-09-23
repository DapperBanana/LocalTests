
import random

def generate_crossword(rows, cols, words):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            col = random.randint(0, cols - len(word))
            row = random.randint(0, rows - 1)
            for i, letter in enumerate(word):
                grid[row][col + i] = letter
        else:
            row = random.randint(0, rows - len(word))
            col = random.randint(0, cols - 1)
            for i, letter in enumerate(word):
                grid[row + i][col] = letter
    
    return grid

rows = 10
cols = 10
words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'RANDOM', 'GENERATE']

crossword = generate_crossword(rows, cols, words)

for row in crossword:
    print(' '.join(row))
