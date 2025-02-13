
def is_isogram(s):
    # Convert the string to lowercase to make the comparison case-insensitive
    s = s.lower()
    
    # Create a set to keep track of the unique letters in the string
    unique_letters = set()
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Check if the character is already in the set
            if char in unique_letters:
                return False
            else:
                unique_letters.add(char)
    
    return True

# Test the function with some examples
print(is_isogram("hello")) # False
print(is_isogram("world")) # True
print(is_isogram("python")) # True
print(is_isogram("apple")) # False
