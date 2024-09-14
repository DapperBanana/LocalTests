
import string

def remove_punctuation(input_str):
    # Create a translation table to map all punctuation characters to None
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove all punctuation from the input string using the translation table
    cleaned_str = input_str.translate(translator)
    
    return cleaned_str

# Test the function with a sample string
sample_string = "Hello, I am a string! With some punctuation."
cleaned_string = remove_punctuation(sample_string)
print(cleaned_string)
