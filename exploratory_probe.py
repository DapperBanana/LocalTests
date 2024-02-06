
import random

def train_model(corpus):
    words = corpus.split()
    model = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word in model:
            model[current_word].append(next_word)
        else:
            model[current_word] = [next_word]
  
    return model

def generate_sentence(model):
    sentence = []
    current_word = random.choice(list(model.keys()))
    sentence.append(current_word)
    
    while current_word in model:
        next_word = random.choice(model[current_word])
        sentence.append(next_word)
        current_word = next_word
        
    return ' '.join(sentence)


# Read the corpus
with open("corpus.txt", "r") as file:
    corpus = file.read()
    

# Train the model
model = train_model(corpus)


# Generate a sentence
sentence = generate_sentence(model)
print(sentence)
