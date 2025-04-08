
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)

sentence = input("Enter a sentence: ")
print("Length of longest word:", find_longest_word(sentence))
