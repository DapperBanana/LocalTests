
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(input_sentence)
print("Reversed sentence:", reversed_sentence)
