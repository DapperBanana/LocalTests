
import string

def remove_punctuation(input_string):
    # Define the set of punctuation characters
    punctuation = string.punctuation
    
    # Remove punctuation characters from the input string
    result = input_string.translate(str.maketrans('', '', punctuation))
    
    return result

# Test the function
input_string = "Hello, World! This is a test."
output_string = remove_punctuation(input_string)
print(output_string)
