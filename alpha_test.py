
def is_isogram(string):
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Create an empty set to store unique characters
    seen = set()
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a letter
        if char.isalpha():
            # If the character is already in the set, return False
            if char in seen:
                return False
            # Otherwise, add the character to the set
            seen.add(char)
    
    # If all characters are unique, return True
    return True

# Test the function with a few examples
print(is_isogram("hello"))  # False
print(is_isogram("world"))  # True
print(is_isogram("Python"))  # True
print(is_isogram("isogram"))  # False
