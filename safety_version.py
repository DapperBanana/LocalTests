
import random

def generate_crossword(words):
    # Find the maximum length of all words
    max_length = max(len(word) for word in words)
    
    # Create an empty grid
    grid = [[' ' for _ in range(max_length)] for _ in range(max_length)]
    
    # Generate a random crossword
    for word in words:
        orientation = random.choice(['horizontal', 'vertical'])
        
        if orientation == 'horizontal':
            # Find a random starting position for a horizontal word
            x = random.randint(0, max_length - len(word))
            y = random.randint(0, max_length - 1)
            
            # Insert the word horizontally
            for i in range(len(word)):
                grid[y][x + i] = word[i]
                
        elif orientation == 'vertical':
            # Find a random starting position for a vertical word
            x = random.randint(0, max_length - 1)
            y = random.randint(0, max_length - len(word))
            
            # Insert the word vertically
            for i in range(len(word)):
                grid[y + i][x] = word[i]
                
    # Display the crossword
    for row in grid:
        print(''.join(row))

# Example usage
words = ['python', 'program', 'crossword', 'random', 'generator']
generate_crossword(words)
