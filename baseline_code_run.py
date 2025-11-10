
import string

def remove_punctuation(input_string):
    punctuation = string.punctuation
    no_punctuation_str = ''
    
    for char in input_string:
        if char not in punctuation:
            no_punctuation_str += char
            
    return no_punctuation_str

input_string = "Hello, World!"
output_string = remove_punctuation(input_string)
print(output_string)  # Output: Hello World
