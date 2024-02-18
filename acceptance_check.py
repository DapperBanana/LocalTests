
import string

def remove_punctuation(input_string):
    return ''.join([char for char in input_string if char not in string.punctuation])

# Test the function
input_string = "Hello, World!"
output_string = remove_punctuation(input_string)
print(output_string)
