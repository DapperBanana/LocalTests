
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = "Hello World! How are you?"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
