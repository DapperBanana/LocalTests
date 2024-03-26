
def longest_word_length(sentence):
    words = sentence.split()
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

sentence = "The quick brown fox jumps over the lazy dog"
print("Length of the longest word:", longest_word_length(sentence))
