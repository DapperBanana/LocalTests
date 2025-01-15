
def is_palindrome_sentence(s):
    s = ''.join([c for c in s.lower() if c.isalnum()])  # removes non-alphanumeric characters and converts to lowercase
    return s == s[::-1]  # checks if the string is equal to its reverse


# Test the program
sentence = "A man, a plan, a canal, Panama!"
if is_palindrome_sentence(sentence):
    print(f"'{sentence}' is a valid palindrome sentence.")
else:
    print(f"'{sentence}' is not a valid palindrome sentence.")
