
def longest_word_length(sentence):
    words = sentence.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

sentence = input("Enter a sentence: ")
length = longest_word_length(sentence)
print(f"The length of the longest word in the sentence is: {length}")
