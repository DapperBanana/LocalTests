
import random

def generate_crossword(rows, cols):
    puzzle = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    words = ['PYTHON', 'CODE', 'PUZZLE', 'COMPUTER', 'PROGRAMMING']
    
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            start_row = random.randint(0, rows - 1)
            start_col = random.randint(0, cols - len(word))
            for i, char in enumerate(word):
                puzzle[start_row][start_col + i] = char
        else:
            start_row = random.randint(0, rows - len(word))
            start_col = random.randint(0, cols - 1)
            for i, char in enumerate(word):
                puzzle[start_row + i][start_col] = char
    
    return puzzle

def display_crossword(puzzle):
    for row in puzzle:
        print(' '.join(row))

if __name__ == '__main__':
    rows = 10
    cols = 10
    puzzle = generate_crossword(rows, cols)
    display_crossword(puzzle)
