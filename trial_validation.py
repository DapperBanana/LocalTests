
import random

def generate_crossword(rows, cols):
    crossword = [['#' for _ in range(cols)] for _ in range(rows)]
    
    words = ['PYTHON', 'PROGRAMMING', 'CROSSWORD', 'PUZZLE', 'RANDOM', 'GENERATOR']
    
    for word in words:
        direction = random.choice(['across', 'down'])
        if direction == 'across':
            x = random.randint(0, cols - len(word))
            y = random.randint(0, rows - 1)
            for i in range(len(word)):
                crossword[y][x + i] = word[i]
        else:
            x = random.randint(0, cols - 1)
            y = random.randint(0, rows - len(word))
            for i in range(len(word)):
                crossword[y + i][x] = word[i]
    
    return crossword

def print_crossword(crossword):
    for row in crossword:
        print(' '.join(row))

if __name__ == '__main__':
    rows = 10
    cols = 10
    
    crossword = generate_crossword(rows, cols)
    print_crossword(crossword)
