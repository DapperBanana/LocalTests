
import random

# Create a dictionary to store the Markov chain transitions
chain = {}

# Sample corpus for training the Markov chain
corpus = "I like to eat ice cream on a hot day"

# Preprocess the corpus
words = corpus.split()
for i in range(len(words) - 1):
    if words[i] in chain:
        chain[words[i]].append(words[i + 1])
    else:
        chain[words[i]] = [words[i + 1]

# Generate a random sentence
sentence = []
word = random.choice(words)
sentence.append(word)
while len(sentence) < 10:  # Generate a sentence with max 10 words
    if word in chain:
        next_word = random.choice(chain[word])
        sentence.append(next_word)
        word = next_word
    else:
        break

# Print the generated sentence
print(" ".join(sentence))
