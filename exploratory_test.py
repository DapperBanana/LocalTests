
import random

def generate_markov_chain(text, n):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        value = words[i+n]
        
        if key in markov_chain:
            markov_chain[key].append(value)
        else:
            markov_chain[key] = [value]
    
    return markov_chain

def generate_sentence(markov_chain, n, length):
    sentence = random.choice(list(markov_chain.keys()))
    
    while len(sentence) < length:
        new_word = random.choice(markov_chain[sentence[-n:]])
        sentence += (new_word,)
    
    return ' '.join(sentence)

text = "This is a sample text to demonstrate the generation of random sentences using Markov chains"
n = 2
length = 10

markov_chain = generate_markov_chain(text, n)
sentence = generate_sentence(markov_chain, n, length)

print(sentence)
