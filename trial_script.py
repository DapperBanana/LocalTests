
def is_isogram(string):
    string = string.lower()
    seen = set()
    for char in string:
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)
    return True

# Test the function
print(is_isogram("hello"))  # False
print(is_isogram("Python")) # True
print(is_isogram("abcdefghijklmnopqrstuvwxyz"))  # True
print(is_isogram("programming"))  # False
