
import random

# Create a dictionary to store the transition probabilities
# between words based on the input text
def create_markov_chain(text):
    words = text.split()
    markov_chain = {}
    for i in range(len(words) - 1):
        if words[i] in markov_chain:
            markov_chain[words[i]].append(words[i + 1])
        else:
            markov_chain[words[i]] = [words[i + 1]]
    return markov_chain

# Generate a random sentence using the Markov chain
def generate_sentence(markov_chain, length=10):
    current_word = random.choice(list(markov_chain.keys()))
    sentence = current_word
    for _ in range(length - 1):
        next_word = random.choice(markov_chain[current_word])
        current_word = next_word
        sentence += ' ' + next_word
    return sentence

# Sample input text
input_text = "The quick brown fox jumps over the lazy dog"

# Create Markov chain
markov_chain = create_markov_chain(input_text)

# Generate random sentence
random_sentence = generate_sentence(markov_chain)

print(random_sentence)
