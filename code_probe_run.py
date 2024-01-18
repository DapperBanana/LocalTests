
import string

def remove_punctuation(text):
    punctuation = string.punctuation
    # Create a translation table using the punctuation characters
    translator = str.maketrans('', '', punctuation)
    # Use the translation table to remove punctuation from the string
    text_without_punct = text.translate(translator)
    return text_without_punct

# Test the function
text = "Hello, World! What's up?"
clean_text = remove_punctuation(text)
print(clean_text)
