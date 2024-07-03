
def is_palindrome(sentence):
    sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    return sentence == sentence[::-1]

input_sentence = input("Enter a sentence to check if it is a palindrome: ")
if is_palindrome(input_sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a palindrome.")
