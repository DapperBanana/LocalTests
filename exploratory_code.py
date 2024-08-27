
import random

def generate_crossword():
    crossword = [[' ' for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            crossword[i][j] = chr(random.randint(65, 90))

    return crossword

def print_crossword(crossword):
    for row in crossword:
        print(' '.join(row))

crossword = generate_crossword()
print_crossword(crossword)
