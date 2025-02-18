
import random

def generate_markov_chain(text, order=2):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - order):
        key = tuple(words[i:i + order])
        value = words[i + order]

        if key in markov_chain:
            markov_chain[key].append(value)
        else:
            markov_chain[key] = [value]

    return markov_chain

def generate_sentence(markov_chain, order=2, length=10):
    seed = random.choice(list(markov_chain.keys()))
    sentence = list(seed)

    for _ in range(length - order):
        next_word = random.choice(markov_chain.get(tuple(sentence[-order:]), ['']))
        sentence.append(next_word)

    return ' '.join(sentence)

if __name__ == '__main__':
    text = "This is a sentence that we use to generate a random sentence using Markov chains."
    markov_chain = generate_markov_chain(text)
    sentence = generate_sentence(markov_chain)
    print(sentence)
