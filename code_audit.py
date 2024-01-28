
def is_palindrome_sentence(sentence):
    # Remove special characters and convert to lower case
    sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Check if the sentence is a palindrome
    return sentence == sentence[::-1]

# Test cases
sentences = ["A man, a plan, a canal, Panama!", "Race car", "Hello world"]

for sentence in sentences:
    if is_palindrome_sentence(sentence):
        print(f"'{sentence}' is a valid palindrome sentence.")
    else:
        print(f"'{sentence}' is not a valid palindrome sentence.")
