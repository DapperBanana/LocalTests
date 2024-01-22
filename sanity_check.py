
def find_longest_word_length(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    longest_word_length = 0
    
    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    
    return longest_word_length


# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print("Length of the longest word:", find_longest_word_length(sentence))
