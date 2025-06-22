
def is_isogram(word):
    word = word.lower()
    unique_chars = set(word)
    return len(word) == len(unique_chars)

word = input("Enter a word: ")
if is_isogram(word):
    print(f"{word} is an isogram.")
else:
    print(f"{word} is not an isogram.")
