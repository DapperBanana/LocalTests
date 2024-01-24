
def reverse_sentence(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words into a new sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


# Test the function with a sample sentence
sentence = "Hello world, how are you?"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
