
import random

# Define a function to generate a Markov chain from a list of words
def generate_markov_chain(text, order=2):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words)-order):
        key = tuple(words[i:i+order])
        value = words[i+order]
        
        if key in markov_chain:
            markov_chain[key].append(value)
        else:
            markov_chain[key] = [value]
    
    return markov_chain

# Define a function to generate a random sentence using a Markov chain
def generate_sentence(markov_chain, length=10):
    current_key = random.choice(list(markov_chain.keys()))
    sentence = list(current_key)
    
    for _ in range(length):
        next_word = random.choice(markov_chain[current_key])
        sentence.append(next_word)
        
        current_key = tuple(sentence[-len(current_key):])
    
    return ' '.join(sentence)

# Input text
text = "I like to eat pizza with cheese and sauce"

# Generate Markov chain from input text
markov_chain = generate_markov_chain(text)

# Generate a random sentence using the Markov chain
random_sentence = generate_sentence(markov_chain, length=10)

print(random_sentence)
