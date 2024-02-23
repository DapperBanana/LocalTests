
import string

def remove_punctuation(text):
    no_punct_text = text.translate(str.maketrans('', '', string.punctuation))
    return no_punct_text

if __name__ == "__main__":
    text = input("Enter a string with punctuation: ")
    result = remove_punctuation(text)
    print("String without punctuation:", result)
