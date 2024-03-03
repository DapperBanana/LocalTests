
def is_palindrome(sentence):
    sentence = ''.join(c for c in sentence if c.isalnum()).lower()
    return sentence == sentence[::-1]

sentence = input("Enter a sentence: ")
if is_palindrome(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
