
def longest_word_length(sentence):
    words = sentence.split()
    longest_length = 0
    
    for word in words:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length
            
    return longest_length

sentence = "The quick brown fox jumps over the lazy dog"
print("The length of the longest word in the sentence is:", longest_word_length(sentence))
