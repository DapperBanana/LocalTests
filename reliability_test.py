
def is_isogram(string):
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Create an empty set to store unique characters
    char_set = set()
    
    for char in string:
        # Check if the character is a letter
        if char.isalpha():
            # If the character is already in the set, return False
            if char in char_set:
                return False
            # Otherwise, add the character to the set
            char_set.add(char)
    
    # If loop completes, return True
    return True

# Test the function with some examples
print(is_isogram("hello"))  # False
print(is_isogram("python"))  # True
print(is_isogram("World"))  # True
