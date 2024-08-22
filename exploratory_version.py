
def is_palindrome(sentence):
    # Remove whitespace and punctuation from the sentence
    sentence = ''.join(c for c in sentence if c.isalnum()).lower()
    
    # Check if the sentence is a palindrome
    return sentence == sentence[::-1]

# Test the function
sentence1 = "A Santa at NASA"
sentence2 = "Was it a car or a cat I saw?"
sentence3 = "Hello World"

if is_palindrome(sentence1):
    print(f"'{sentence1}' is a palindrome")
else:
    print(f"'{sentence1}' is not a palindrome")

if is_palindrome(sentence2):
    print(f"'{sentence2}' is a palindrome")
else:
    print(f"'{sentence2}' is not a palindrome")

if is_palindrome(sentence3):
    print(f"'{sentence3}' is a palindrome")
else:
    print(f"'{sentence3}' is not a palindrome")
