
def is_isogram(s):
    # Convert the string to lowercase to make case insensitive
    s = s.lower()
    
    # Create a set to store unique characters
    unique_chars = set()
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # If the character is already in the set, return False
            if char in unique_chars:
                return False
            # Otherwise, add it to the set
            else:
                unique_chars.add(char)
    
    # If no repeating characters were found, return True
    return True

# Test the function with some example strings
print(is_isogram("hello"))  # False
print(is_isogram("world"))  # True
print(is_isogram("Programming"))  # True
