
import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    input_string = "Hello, World! This is a test string."
    result = remove_punctuation(input_string)
    print(result)
