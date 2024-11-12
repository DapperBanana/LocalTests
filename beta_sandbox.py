
import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    clean_string = input_string.translate(translator)
    return clean_string

input_string = "Hello, World! How are you doing?"
output_string = remove_punctuation(input_string)
print(output_string)
