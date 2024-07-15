
def longest_word_length(sentence):
    # Split the sentence into individual words
    words = sentence.split()
    
    # Initialize a variable to keep track of the length of the longest word
    max_length = 0
    
    # Iterate through each word to find the longest word
    for word in words:
        length = len(word)
        if length > max_length:
            max_length = length
    
    return max_length

# Get input sentence from user
sentence = input("Enter a sentence: ")

# Call the function and print the result
print("The length of the longest word in the sentence is:", longest_word_length(sentence))
