
import string

def remove_punctuation(input_string):
    # Create a string of all punctuation characters
    punctuation = string.punctuation

    # Remove the punctuation characters from the input string
    no_punct = ""
    for char in input_string:
        if char not in punctuation:
            no_punct += char

    return no_punct

# Example usage
string_with_punct = "Hello, World!"
string_without_punct = remove_punctuation(string_with_punct)
print(string_without_punct)
