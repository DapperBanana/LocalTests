
def is_palindrome(sentence):
    # Removing spaces and converting to lowercase
    sentence = sentence.replace(" ", "").lower()

    # Reversing the string
    reversed_sentence = sentence[::-1]

    # Checking if the original and reversed strings are the same
    if sentence == reversed_sentence:
        return True
    else:
        return False

# Input string
input_string = "A man a plan a canal Panama"

# Checking if the input string is a palindrome
if is_palindrome(input_string):
    print("The input string is a valid palindrome sentence.")
else:
    print("The input string is not a valid palindrome sentence.")
