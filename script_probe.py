
def find_longest_word_length(sentence):
    words = sentence.split()
    longest_length = 0
    
    for word in words:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length
            
    return longest_length

sentence = input("Enter a sentence: ")
result = find_longest_word_length(sentence)
print(f"The length of the longest word in the sentence is: {result}")
