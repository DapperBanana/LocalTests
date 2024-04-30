
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

sentence = "Hello world how are you"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)
