
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

input_string = "Hello, World! How are you today?" 
clean_string = remove_punctuation(input_string)
print(clean_string)
