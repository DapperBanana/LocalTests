
def is_palindrome(sentence):
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    reversed_sentence = cleaned_sentence[::-1]
    
    return cleaned_sentence == reversed_sentence

sentence = input("Enter a sentence: ")

if is_palindrome(sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
