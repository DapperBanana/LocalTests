
import string

def remove_punctuation(s):
    # Define a set of punctuation characters
    punctuation = set(string.punctuation)

    # Remove punctuation characters from the string
    result = ''.join(char for char in s if char not in punctuation)

    return result

# Take user input for the string
input_string = input("Enter a string: ")

# Remove punctuation from the input string
output = remove_punctuation(input_string)

# Print the string without punctuation
print("String without punctuation:", output)
