
import random

def generate_markov_chain(text, n):
    words = text.split()
    markov_chain = {}

    for i in range(len(words)-n):
        key = tuple(words[i:i+n])
        value = words[i+n]
        if key in markov_chain:
            markov_chain[key].append(value)
        else:
            markov_chain[key] = [value]

    return markov_chain

def generate_random_sentence(markov_chain, n, length):
    current_key = random.choice(list(markov_chain.keys()))
    sentence = ' '.join(current_key)

    for _ in range(length):
        if current_key in markov_chain:
            next_word = random.choice(markov_chain[current_key])
            sentence += ' ' + next_word
            current_key = tuple(list(current_key[1:]) + [next_word])
        else:
            break

    return sentence

text = "This is a sample text to generate a random sentence using Markov chains"
n = 2
length = 10

markov_chain = generate_markov_chain(text, n)
random_sentence = generate_random_sentence(markov_chain, n, length)

print(random_sentence)
