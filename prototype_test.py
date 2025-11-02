
import random

def generate_crossword(rows, cols):
    words = ["PYTHON", "PROGRAM", "CROSSWORD", "PUZZLE", "RANDOM", "GENERATE"]
    crossword = [[' ' for _ in range(cols)] for _ in range(rows)]

    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            while True:
                start_row = random.randint(0, rows-1)
                start_col = random.randint(0, cols-len(word))
                if all(crossword[start_row][start_col+i] == ' ' for i in range(len(word))):
                    for i in range(len(word)):
                        crossword[start_row][start_col+i] = word[i]
                    break
        else:
            while True:
                start_row = random.randint(0, rows-len(word))
                start_col = random.randint(0, cols-1)
                if all(crossword[start_row+i][start_col] == ' ' for i in range(len(word))):
                    for i in range(len(word)):
                        crossword[start_row+i][start_col] = word[i]
                    break

    return crossword

def print_crossword(crossword):
    for row in crossword:
        print(' '.join(row))

rows = 10
cols = 10
crossword = generate_crossword(rows, cols)
print_crossword(crossword)
