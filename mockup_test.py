
def find_longest_word(sentence):
    words = sentence.split()
    longest_word_length = 0
    
    for word in words:
        word_length = len(word)
        if word_length > longest_word_length:
            longest_word_length = word_length
    
    return longest_word_length

sentence = input("Enter a sentence: ")
print("The length of the longest word in the sentence is:", find_longest_word(sentence))
