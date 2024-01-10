
import random

def generate_sentence(corpus, num_words):
    words = corpus.split()
    chain = {}

    # Build Markov chain
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]

        if current_word not in chain:
            chain[current_word] = []
        chain[current_word].append(next_word)

    # Generate sentence
    word = random.choice(words)
    sentence = [word]

    for _ in range(num_words - 1):
        word = random.choice(chain[word])
        sentence.append(word)

    return ' '.join(sentence)

corpus = "I am happy today because it is sunny outside"
num_words = 10

sentence = generate_sentence(corpus, num_words)
print(sentence)
