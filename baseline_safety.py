
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(sentence)
print("Reversed sentence: ", reversed_sentence)
