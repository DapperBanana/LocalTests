
def is_palindrome(sentence):
    # Remove spaces and punctuation
    sentence = ''.join(e for e in sentence if e.isalnum()).lower()
    
    # Check if the sentence is a palindrome
    return sentence == sentence[::-1]

# Get user input
input_sentence = input("Enter a sentence: ")

# Check if the input sentence is a valid palindrome
if is_palindrome(input_sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
