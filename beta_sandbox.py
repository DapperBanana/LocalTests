
import string

def remove_punctuation(input_string):
    # Define all punctuations
    punctuations = string.punctuation

    # Remove punctuation from input string
    cleaned_string = ''.join(char for char in input_string if char not in punctuations)

    return cleaned_string

# Input string with punctuation
input_string = "Hello, World! How are you?"

# Remove punctuation from input string
cleaned_string = remove_punctuation(input_string)

print("Original String:", input_string)
print("String without Punctuation:", cleaned_string)
