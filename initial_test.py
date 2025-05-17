
def is_isogram(word):
    word = word.lower()
    seen = set()
    
    for letter in word:
        if letter.isalpha():
            if letter in seen:
                return False
            seen.add(letter)
    
    return True

# Test the function
word = input("Enter a word: ")
if is_isogram(word):
    print(f"{word} is an isogram.")
else:
    print(f"{word} is not an isogram.")
