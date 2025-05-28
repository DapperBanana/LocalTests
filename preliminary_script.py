
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Get input from user
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)

print("Number of vowels in the given string: ", vowel_count)
