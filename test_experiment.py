
import random

def create_markov_chain(text, n=2):
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

def generate_sentence(markov_chain, n=2, length=10):
    start = random.choice(list(markov_chain.keys()))
    sentence = list(start)

    while len(sentence) < length:
        next_word = random.choice(markov_chain[tuple(sentence[-n:])])
        sentence.append(next_word)

    return ' '.join(sentence)

if __name__ == '__main__':
    text = "This is a sample text for generating random sentences using Markov chains"
    markov_chain = create_markov_chain(text)

    for _ in range(3):  # Generate 3 random sentences
        sentence = generate_sentence(markov_chain)
        print(sentence)
