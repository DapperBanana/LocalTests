
def find_longest_word(sentence):
    words = sentence.split()
    max_length = 0
    longest_word = ''
    
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
            
    return max_length, longest_word

sentence = input("Enter a sentence: ")
length, longest_word = find_longest_word(sentence)
print(f"The longest word in the sentence is '{longest_word}' with a length of {length} characters.")
