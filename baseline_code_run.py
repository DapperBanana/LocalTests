
import random

def generate_crossword(width, height):
    crossword = [[' ' for _ in range(width)] for _ in range(height)]
    words = ['apple', 'banana', 'cherry', 'orange', 'grape', 'pear']

    for word in words:
        direction = random.choice(['across', 'down'])
        if direction == 'across':
            x = random.randint(0, width - len(word))
            y = random.randint(0, height - 1)
            for i in range(len(word)):
                crossword[y][x + i] = word[i]
        else:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - len(word))
            for i in range(len(word)):
                crossword[y + i][x] = word[i]

    return crossword

def print_crossword(crossword):
    for row in crossword:
        print(''.join(row))

if __name__ == "__main__":
    width = 10
    height = 10
    crossword = generate_crossword(width, height)
    print_crossword(crossword)
