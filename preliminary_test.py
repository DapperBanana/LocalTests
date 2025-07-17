
def is_palindrome(sentence):
    # Remove all non-alphanumeric characters from the sentence
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    # Check if the cleaned sentence is equal to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]

# Take input from the user
sentence = input("Enter a sentence: ")

# Check if the input sentence is a palindrome
if is_palindrome(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a palindrome.")
