
def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))

word = input("Enter a word: ")
if is_isogram(word):
    print(f"{word} is an isogram.")
else:
    print(f"{word} is not an isogram.")
