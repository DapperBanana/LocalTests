
import string

def remove_punctuation(input_str):
    # Create a string containing all punctuation marks
    punctuations = string.punctuation

    # Remove all punctuation marks from the input string
    output_str = ''.join(char for char in input_str if char not in punctuations)

    return output_str

# Test the function with a sample input
input_string = "Hello, World! How are you today?"
output_string = remove_punctuation(input_string)
print(output_string)
