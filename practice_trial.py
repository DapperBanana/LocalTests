
def count_word_occurrences(input_string):
    # Split the input string into individual words
    words = input_string.split()

    # Create a dictionary to store word occurrences
    word_counts = {}

    # Iterate through each word and update the word counts
    for word in words:
        # Remove any punctuation from the word
        word = word.strip('.,!?()[]{}:;\"\'')
        # Convert the word to lowercase to ensure case-insensitivity
        word = word.lower()
        # Update the word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print the word occurrences
    for word, count in word_counts.items():
        print(f'{word}: {count}')

# Get the input string from the user
input_string = input("Enter a string: ")

# Call the count_word_occurrences function
count_word_occurrences(input_string)
