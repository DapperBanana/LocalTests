
import string

def remove_punctuation(text):
    punctuation = string.punctuation
    clean_text = ''
    
    for char in text:
        if char not in punctuation:
            clean_text += char
    
    return clean_text

# Example usage
text = "Hello, World! How are you?"
clean_text = remove_punctuation(text)
print(clean_text)
