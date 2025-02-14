
import random

# Function to generate a random crossword puzzle of size n x n
def generate_crossword(n):
    puzzle = [[' ' for _ in range(n)] for _ in range(n)]
    
    num_words = random.randint(n//2, n)
    
    for _ in range(num_words):
        word = ''.join([chr(random.randint(97, 122)) for _ in range(random.randint(3, n//2))])
        direction = random.choice(['across', 'down'])
        
        if direction == 'across':
            row = random.randint(0, n-1)
            col = random.randint(0, n-len(word))
            for i in range(len(word)):
                puzzle[row][col+i] = word[i]
        elif direction == 'down':
            row = random.randint(0, n-len(word))
            col = random.randint(0, n-1)
            for i in range(len(word)):
                puzzle[row+i][col] = word[i]
    
    return puzzle

# Function to print the crossword puzzle
def print_crossword(puzzle):
    for row in puzzle:
        print(' '.join(row))

# Generate a crossword puzzle of size 10 x 10
n = 10
puzzle = generate_crossword(n)

print_crossword(puzzle)
