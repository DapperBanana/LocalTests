
import random

# Sample transition matrix for Markov chain
transition_matrix = {
    'I': {'love': 0.5, 'hate': 0.5},
    'love': {'coding': 0.5, 'python': 0.5},
    'hate': {'bugs': 0.5, 'spiders': 0.5},
    'coding': {'is': 1.0},
    'is': {'fun': 1.0},
    'python': {'programming': 1.0},
    'bugs': {'are': 1.0},
    'are': {'annoying': 1.0},
    'spiders': {'are': 1.0},
    'annoying': {'.': 1.0}
}

def generate_sentence(matrix):
    sentence = []
    word = 'I'
    
    while True:
        sentence.append(word)
        if word in matrix:
            next_word = random.choices(list(matrix[word].keys()), list(matrix[word].values()))[0]
        else:
            break

        if next_word == '.':
            break
            
        word = next_word
        
    return ' '.join(sentence)

random_sentence = generate_sentence(transition_matrix)
print(random_sentence)
