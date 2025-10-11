
def longest_word_length(sentence):
    words = sentence.split()
    max_length = max([len(word) for word in words])
    return max_length

sentence = input("Enter a sentence: ")
length = longest_word_length(sentence)
print("The length of the longest word in the sentence is:", length)
