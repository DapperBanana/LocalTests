
import random

def generate_crossword(size):
    crossword = [['_' for _ in range(size)] for _ in range(size)]
    
    # Generate random words of random lengths
    words = ['apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi', 'lemon']
    random.shuffle(words)
    
    for word in words:
        x = random.randint(0, size - len(word))
        y = random.randint(0, size - len(word))
        
        for i in range(len(word)):
            crossword[y][x+i] = word[i]
        
    return crossword

def print_crossword(crossword):
    for row in crossword:
        print(' '.join(row))

size = int(input("Enter the size of the crossword: "))
crossword = generate_crossword(size)
print("Generated Crossword Puzzle:")
print_crossword(crossword)
