
import string

def remove_punctuation(input_string):
    no_punct = ""
    for char in input_string:
        if char not in string.punctuation:
            no_punct += char
    return no_punct

input_string = "Hello, World! How are you?"
output_string = remove_punctuation(input_string)
print(output_string)
