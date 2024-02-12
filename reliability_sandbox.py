
def is_isogram(word):
    # Convert the word to lowercase
    word = word.lower()
    
    # Create an empty set to store the unique letters
    unique_letters = set()
    
    # Iterate over each letter in the word
    for letter in word:
        # If the letter is already in the unique_letters set, the word is not an isogram
        if letter in unique_letters:
            return False
        # Otherwise, add the letter to the set
        else:
            unique_letters.add(letter)
    
    # If all letters are unique, the word is an isogram
    return True

# Test the function with some examples
print(is_isogram("hello"))  # False
print(is_isogram("python"))  # True
print(is_isogram("world"))  # False
print(is_isogram("programming"))  # False
