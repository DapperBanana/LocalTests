
def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the length of both strings is equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in each string and compare them
    return sorted(str1) == sorted(str2)

# Test the function with some examples
str1 = "Listen"
str2 = "Silent"
print(f"{str1} and {str2} are anagrams: {is_anagram(str1, str2)}")

str1 = "hello"
str2 = "world"
print(f"{str1} and {str2} are anagrams: {is_anagram(str1, str2)}")
