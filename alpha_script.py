
def is_isogram(word):
    word = word.lower()
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True

input_word = input("Enter a word or phrase: ")

if is_isogram(input_word):
    print(f"{input_word} is an isogram.")
else:
    print(f"{input_word} is not an isogram.")
