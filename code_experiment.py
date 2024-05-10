
import string

def remove_punctuation(input_string):
    output_string = ""
    for char in input_string:
        if char not in string.punctuation:
            output_string += char
    return output_string

input_string = "Hello, World! How are you?"
output_string = remove_punctuation(input_string)
print(output_string)
