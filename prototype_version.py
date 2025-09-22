
import random

def generate_markov_chain(text, order):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words) - order):
        key = tuple(words[i:i+order])
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(words[i+order])
        
    return markov_chain

def generate_sentence(markov_chain, order, length):
    words = random.choice(list(markov_chain.keys()))
    sentence = ' '.join(words)
    
    for _ in range(length):
        key = tuple(words[-order:])
        if key in markov_chain:
            next_word = random.choice(markov_chain[key])
            words = words[1:] + (next_word,)
            sentence += ' ' + next_word
        else:
            break
    
    return sentence

text = "Hello world. This is a Python Markov chain generator. It generates random sentences based on input text."

order = 2
length = 10

markov_chain = generate_markov_chain(text, order)
sentence = generate_sentence(markov_chain, order, length)

print(sentence)
