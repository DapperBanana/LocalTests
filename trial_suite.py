
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print("Reversed sentence:", reversed_sentence)
