
def is_palindrome(sentence):
    sentence = sentence.lower().replace(" ", "").replace(",", "").replace(".", "")
    reversed_sentence = sentence[::-1]
    
    return sentence == reversed_sentence

input_sentence = input("Enter a sentence: ")

if is_palindrome(input_sentence):
    print("The sentence is a valid palindrome.")
else:
    print("The sentence is not a valid palindrome.")
