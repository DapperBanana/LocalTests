
def is_palindrome(sentence):
    sentence = sentence.lower()
    sentence = ''.join(e for e in sentence if e.isalnum())
    return sentence == sentence[::-1]

def main():
    sentence = input("Enter a sentence to check if it is a palindrome: ")
    
    if is_palindrome(sentence):
        print("The sentence is a valid palindrome.")
    else:
        print("The sentence is not a valid palindrome.")

if __name__ == "__main__":
    main()
