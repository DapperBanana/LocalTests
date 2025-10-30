
def longest_word_length(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)

sentence = input("Enter a sentence: ")
length = longest_word_length(sentence)
print(f"The length of the longest word in the sentence is: {length}")
