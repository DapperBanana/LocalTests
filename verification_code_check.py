
def find_longest_word_length(sentence):
    words = sentence.split()
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length

sentence = input("Enter a sentence: ")
longest_word_length = find_longest_word_length(sentence)
print("Length of the longest word:", longest_word_length)
