
def longest_word_length(sentence):
    words = sentence.split()
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length

sentence = input("Enter a sentence: ")
length = longest_word_length(sentence)
print(f"The length of the longest word in the sentence is: {length}")
