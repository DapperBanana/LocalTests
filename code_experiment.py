
import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

input_string = "Hello, World! This is a sample sentence."

output_string = remove_punctuation(input_string)
print(output_string)
