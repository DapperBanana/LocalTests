
import string

def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

input_string = "Hello, world! How are you?"

cleaned_string = remove_punctuation(input_string)
print(cleaned_string)
