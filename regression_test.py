
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Test the function
text = "Hello, world! This is a test string."
clean_text = remove_punctuation(text)
print(clean_text)
