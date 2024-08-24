
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Taking user input
sentence = input("Enter a sentence: ")

# Reversing the order of words in the sentence
reversed_sentence = reverse_sentence(sentence)

# Displaying the reversed sentence
print("Reversed sentence: ", reversed_sentence)
