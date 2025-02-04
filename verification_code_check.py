
import string

def remove_punctuation(input_string):
    # Define the punctuation characters
    punctuations = string.punctuation

    # Remove punctuation characters from the input string
    output_string = ''.join(char for char in input_string if char not in punctuations)

    return output_string

# Get the input string from the user
input_string = input("Enter a string: ")

# Remove punctuation from the input string
output_string = remove_punctuation(input_string)

print("String without punctuation: ", output_string)
