
def is_palindrome_sentence(sentence):
    sentence = ''.join(filter(str.isalnum, sentence)).lower()
    return sentence == sentence[::-1]

# Test the function
sentence1 = "A man, a plan, a canal, Panama"
sentence2 = "Was it a car or a cat I saw?"
sentence3 = "Hello, World!"

if is_palindrome_sentence(sentence1):
    print(f"'{sentence1}' is a valid palindrome sentence")
else:
    print(f"'{sentence1}' is not a valid palindrome sentence")

if is_palindrome_sentence(sentence2):
    print(f"'{sentence2}' is a valid palindrome sentence")
else:
    print(f"'{sentence2}' is not a valid palindrome sentence")

if is_palindrome_sentence(sentence3):
    print(f"'{sentence3}' is a valid palindrome sentence")
else:
    print(f"'{sentence3}' is not a valid palindrome sentence")
