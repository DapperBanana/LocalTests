
import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

# Example usage
text = "Hello, World! How are you doing today?"
clean_text = remove_punctuation(text)

print(clean_text)
