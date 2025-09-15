
def is_palindrome_sentence(input_string):
    # Removing all non-alphabet characters from the input string and converting it to lowercase
    input_string = "".join(char.lower() for char in input_string if char.isalpha())
    
    # Checking if the string is a palindrome
    return input_string == input_string[::-1]

# Taking user input
sentence = input("Enter a sentence to check if it is a palindrome: ")

# Checking if the sentence is a palindrome
if is_palindrome_sentence(sentence):
    print("The entered sentence is a palindrome.")
else:
    print("The entered sentence is not a palindrome.")
