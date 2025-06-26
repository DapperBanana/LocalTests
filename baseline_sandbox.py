
def is_isogram(string):
    string = string.lower()  # Convert string to lowercase

    # Check for repeating characters
    for char in string:
        if string.count(char) > 1:
            return False

    return True

# Test the function with a few examples
print(is_isogram("hello"))  # False
print(is_isogram("world"))  # True
print(is_isogram("programming"))  # True
