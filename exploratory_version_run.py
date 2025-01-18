
def find_longest_word_length(sentence):
    words = sentence.split()
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length

sentence = input("Enter a sentence: ")
length_of_longest_word = find_longest_word_length(sentence)
print(f"The length of the longest word in the sentence is: {length_of_longest_word}")
