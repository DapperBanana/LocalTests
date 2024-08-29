
def is_palindrome_sentence(sentence):
    filtered_sentence = ''.join(char for char in sentence.lower() if char.isalnum())
    return filtered_sentence == filtered_sentence[::-1]

# Test the function
sentence = "A Santa at NASA"
if is_palindrome_sentence(sentence):
    print(f"'{sentence}' is a valid palindrome sentence.")
else:
    print(f"'{sentence}' is not a valid palindrome sentence.")
