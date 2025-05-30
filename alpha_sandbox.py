
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    return clean_text

input_string = "Hello, World! How are you today?"
clean_string = remove_punctuation(input_string)
print(clean_string)
