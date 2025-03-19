
def is_palindrome(sentence):
    sentence = sentence.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    reversed_sentence = sentence[::-1]
    return sentence == reversed_sentence

def main():
    sentence = input("Enter a sentence: ")
    if is_palindrome(sentence):
        print("The sentence is a valid palindrome.")
    else:
        print("The sentence is not a valid palindrome.")

if __name__ == "__main__":
    main()
