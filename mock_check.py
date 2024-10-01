
def is_palindrome_sentence(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char for char in s if char.isalnum()).lower()
    
    # Check if cleaned string is a palindrome
    return cleaned_string == cleaned_string[::-1]

# Test the function
sentence = "A man, a plan, a canal, Panama"
if is_palindrome_sentence(sentence):
    print(f"'{sentence}' is a valid palindrome sentence.")
else:
    print(f"'{sentence}' is not a valid palindrome sentence.")
