
def is_palindrome_sentence(s):
    # Remove all spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
sentence = input("Enter a sentence: ")

if is_palindrome_sentence(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a palindrome.")
