
def longest_word(sentence):
    words = sentence.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

sentence = input("Enter a sentence: ")
longest_word_length = longest_word(sentence)
print("The length of the longest word in the sentence is:", longest_word_length)
