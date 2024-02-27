
def is_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters in the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Check if the sorted strings are equal
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Test the function with some examples
print(is_anagram("listen", "silent")) # True
print(is_anagram("hello", "world"))   # False
print(is_anagram("Astronomer", "Moon starer"))   # True
