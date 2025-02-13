
import random

def generate_crossword(rows, cols):

    crossword = [[' ' for _ in range(cols)] for _ in range(rows)]

    word_list = ['PYTHON', 'PROGRAMMING', 'CROSSWORD', 'PUZZLE', 'RANDOM', 'GENERATE']

    for word in word_list:
        direction = random.choice(['across', 'down'])
        if direction == 'across':
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - len(word))
            for i in range(len(word)):
                crossword[row][col + i] = word[i]
        else:
            row = random.randint(0, rows - len(word))
            col = random.randint(0, cols - 1)
            for i in range(len(word)):
                crossword[row + i][col] = word[i]

    for row in crossword:
        print(''.join(row))

rows = 10
cols = 10

generate_crossword(rows, cols)
