
def is_isogram(string):
    string = string.lower()
    char_count = {}

    for char in string:
        if char.isalpha():
            if char in char_count:
                return False
            char_count[char] = 1

    return True

# Test the function
print(is_isogram("hello"))  # False
print(is_isogram("world"))  # True
print(is_isogram("python"))  # True
print(is_isogram("programming"))  # False
