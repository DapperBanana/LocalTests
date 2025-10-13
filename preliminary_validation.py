
import string

def remove_punctuation(text):
    no_punctuation = ""
    for char in text:
        if char not in string.punctuation:
            no_punctuation += char
    return no_punctuation

input_string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)
