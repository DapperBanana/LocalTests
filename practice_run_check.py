
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Test the function
text = "Hello! How are you doing today?"
clean_text = remove_punctuation(text)
print(clean_text)
