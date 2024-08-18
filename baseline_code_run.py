
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Test the function
input_string = "Hello, world! How are you?"
output_string = remove_punctuation(input_string)
print(output_string)
