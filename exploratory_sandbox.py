
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)

sentence = input("Enter a sentence: ")
length = find_longest_word(sentence)
print(f"The length of the longest word in the sentence is: {length}")
