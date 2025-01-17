
def is_isogram(word):
    word = word.lower()
    letters = [letter for letter in word if letter.isalpha()]
    return len(letters) == len(set(letters))

# Test the function
word1 = "isogram"
word2 = "hello"
word3 = "Alphabet"

print(f"{word1} is an isogram: {is_isogram(word1)}")
print(f"{word2} is an isogram: {is_isogram(word2)}")
print(f"{word3} is an isogram: {is_isogram(word3)}")
