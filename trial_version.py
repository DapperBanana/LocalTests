
def reverse_words(sentence):
    words = sentence.split()  # split the sentence into a list of words
    reversed_sentence = ' '.join(reversed(words))  # reverse the list of words and join them back together
    return reversed_sentence

# test the function
sentence = "Hello World"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)
