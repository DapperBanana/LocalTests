
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Taking input from user
input_string = input("Enter a string: ")

# Counting vowels in the input string
vowel_count = count_vowels(input_string)

print("Number of vowels in the string:", vowel_count)
