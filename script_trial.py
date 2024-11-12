
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Input string from user
input_string = input("Enter a string: ")

# Count the number of vowels in the input string
num_vowels = count_vowels(input_string)

print(f"The number of vowels in the string is: {num_vowels}")
