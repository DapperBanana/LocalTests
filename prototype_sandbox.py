
import random

def generate_markov_chain(corpus):
    words = corpus.split()
    chain = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word in chain:
            chain[current_word].append(next_word)
        else:
            chain[current_word] = [next_word]
    
    return chain

def generate_sentence(corpus, length=10):
    chain = generate_markov_chain(corpus)
    words = corpus.split()
    
    current_word = random.choice(words)
    sentence = current_word
    
    for _ in range(length - 1):
        if current_word in chain:
            next_word = random.choice(chain[current_word])
            current_word = next_word
            sentence += " " + current_word
        else:
            break
    
    return sentence

corpus = "I love programming in Python programming is fun and challenging"
sentence = generate_sentence(corpus, 10)
print(sentence)
