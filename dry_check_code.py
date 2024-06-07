
import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

# Input string
input_string = "Hello, how are you doing today?"

# Remove punctuation
output_string = remove_punctuation(input_string)

print(output_string)
