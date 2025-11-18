
def is_palindrome_sentence(sentence):
    # Remove all non-alphanumeric characters and convert to lower case
    cleaned_sentence = ''.join(char for char in sentence if char.isalnum()).lower()

    # Check if the cleaned sentence is a palindrome
    return cleaned_sentence == cleaned_sentence[::-1]

# Get input from the user
input_sentence = input("Enter a sentence: ")

if is_palindrome_sentence(input_sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
