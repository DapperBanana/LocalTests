
import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

input_string = "Hello, World! This is a sample sentence."

output_string = remove_punctuation(input_string)
print(output_string)
