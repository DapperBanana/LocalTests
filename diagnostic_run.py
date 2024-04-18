
def is_palindrome_sentence(sentence):
    # Remove spaces and convert to lowercase
    sentence = sentence.replace(" ", "").lower()
    
    # Check if the sentence is a palindrome
    if sentence == sentence[::-1]:
        return True
    else:
        return False

# Get user input
sentence = input("Enter a sentence: ")

# Check if the input is a valid palindrome sentence
if is_palindrome_sentence(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
