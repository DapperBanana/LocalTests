
def is_anagram(string1, string2):
    # Convert both strings to lowercase and remove spaces
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    # Sort the characters of both strings
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    # Check if the sorted strings are equal
    if sorted_string1 == sorted_string2:
        return True
    else:
        return False

# Test the program
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
