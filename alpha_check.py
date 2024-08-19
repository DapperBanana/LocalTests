
import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

# Input string with punctuation
input_string = "Hello, World! This is a test string."

# Remove punctuation
result_string = remove_punctuation(input_string)

print("Original string:")
print(input_string)
print("\nString after removing punctuation:")
print(result_string)
