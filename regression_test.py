
import nltk
import random

# Download the 'punkt' package to tokenize the text
nltk.download('punkt')

def generate_sentence(tokens):
    # Create a dictionary to store the word transitions
    transitions = {}

    # Iterate over the tokens and create a transition dictionary
    for i in range(len(tokens)-2):
        prefix = (tokens[i], tokens[i+1])
        suffix = tokens[i+2]
        if prefix in transitions:
            transitions[prefix].append(suffix)
        else:
            transitions[prefix] = [suffix]

    # Initialize the current state with a random prefix from the transition dictionary
    state = random.choice(list(transitions.keys()))
    sentence = list(state)

    # Generate the rest of the sentence based on the transition dictionary
    for _ in range(10):
        if state in transitions:
            possible_suffixes = transitions[state]
            suffix = random.choice(possible_suffixes)
            sentence.append(suffix)
            state = (state[1], suffix)
        else:
            break

    # Convert the list of words to a sentence
    sentence = ' '.join(sentence)
    return sentence.capitalize() + '.'

# Load the text corpus
text = nltk.corpus.inaugural.words('2012-Obama.txt')

# Tokenize the text
tokens = nltk.word_tokenize(' '.join(text))

# Generate a random sentence
random_sentence = generate_sentence(tokens)
print(random_sentence)
