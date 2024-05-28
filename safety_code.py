
def is_palindrome_sentence(sentence):
    sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    return sentence == sentence[::-1]

# Test the function
sentence = "A man, a plan, a canal, Panama"
if is_palindrome_sentence(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
