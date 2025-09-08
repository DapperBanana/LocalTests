
import random

def generate_sentence(text, n=2, max_length=20):
    words = text.split()
    ngrams = zip(*[words[i:] for i in range(n)])
    markov_dict = {}
    
    for ngram in ngrams:
        key = ' '.join(ngram[:-1])
        value = ngram[-1]
        
        if key in markov_dict:
            markov_dict[key].append(value)
        else:
            markov_dict[key] = [value]
    
    current_key = random.choice(list(markov_dict.keys()))
    sentence = current_key

    while len(sentence.split()) < max_length:
        if current_key in markov_dict:
            next_word = random.choice(markov_dict[current_key])
            current_key = ' '.join(current_key.split()[1:] + [next_word])
            sentence += ' ' + next_word
        else:
            break
    
    return sentence

text = "This is a simple text to use as an example for the Markov chain generator"
sentence = generate_sentence(text)
print(sentence)
