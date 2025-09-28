
import random

def generate_crossword(size):
    crossword = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Generate random words to fill in the puzzle
    words = ["apple", "banana", "cherry", "orange", "grape", "lemon"]
    
    for word in words:
        orientation = random.choice(['horizontal', 'vertical'])
        
        if orientation == 'horizontal':
            row = random.randint(0, size-1)
            col = random.randint(0, size-len(word))
            
            for i in range(len(word)):
                crossword[row][col+i] = word[i]
                
        elif orientation == 'vertical':
            row = random.randint(0, size-len(word))
            col = random.randint(0, size-1)
            
            for i in range(len(word)):
                crossword[row+i][col] = word[i]
    
    # Print the crossword puzzle
    for row in crossword:
        print(' '.join(row))

# Generate a 10x10 crossword puzzle
generate_crossword(10)
