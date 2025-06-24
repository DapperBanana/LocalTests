
def is_isogram(word):
    word = word.lower()
    seen_letters = []
    
    for letter in word:
        if letter.isalpha():
            if letter in seen_letters:
                return False
            seen_letters.append(letter)
    
    return True

word = input("Enter a word: ")
if is_isogram(word):
    print(f"{word} is an isogram.")
else:
    print(f"{word} is not an isogram.")
