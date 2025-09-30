
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(sentence)
print("Reversed sentence: ", reversed_sentence)
