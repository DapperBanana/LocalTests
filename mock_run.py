
def longest_word_length(sentence):
    words = sentence.split(" ")
    max_length = 0
    
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
    
    return max_length

sentence = input("Enter a sentence: ")
print("The length of the longest word in the sentence is:", longest_word_length(sentence))
