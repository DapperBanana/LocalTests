
import random

def generate_sentence(data, order=1, sentence_length=10):
    # Create n-grams
    ngrams = {}
    for sentence in data:
        words = sentence.split()
        for i in range(len(words) - order):
            gram = ' '.join(words[i:i+order])
            if gram not in ngrams:
                ngrams[gram] = []
            ngrams[gram].append(words[i+order])
    
    # Generate sentence
    current_gram = random.choice(list(ngrams.keys()))
    sentence = current_gram.capitalize()
    for _ in range(sentence_length - order):
        if current_gram not in ngrams:
            break
        possible_words = ngrams[current_gram]
        next_word = random.choice(possible_words)
        sentence += " " + next_word
        words = sentence.split()
        current_gram = ' '.join(words[-order:])
    
    return sentence + "."

# Example usage
data = [
    "I like apples",
    "I like oranges",
    "Oranges are juicy",
    "Oranges are delicious",
    "I like bananas"
]

sentence = generate_sentence(data, order=2, sentence_length=8)
print(sentence)
