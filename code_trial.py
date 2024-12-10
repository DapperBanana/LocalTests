
def longest_word_length(sentence):
    # Split the sentence into individual words
    words = sentence.split()
    
    # Initialize a variable to store the length of the longest word
    max_length = 0
    
    # Iterate through the list of words
    for word in words:
        # Check if the length of the current word is greater than the current max_length
        if len(word) > max_length:
            max_length = len(word)
    
    return max_length

# Input sentence from the user
sentence = input("Enter a sentence: ")

# Call the function and print the result
print("The length of the longest word in the sentence is:", longest_word_length(sentence))
