
def is_palindrome(sentence):
    # Remove spaces and convert to lowercase
    sentence = sentence.replace(" ", "").lower()
    
    # Check if the sentence is a palindrome
    if sentence == sentence[::-1]:
        return True
    else:
        return False

# Get input from the user
sentence = input("Enter a sentence: ")

# Check if the input is a valid palindrome sentence
if is_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")
