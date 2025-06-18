
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Test the function
text = "Hello, World! How are you?"
clean_text = remove_punctuation(text)
print(clean_text)
