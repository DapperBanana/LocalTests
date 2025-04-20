
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Input string
input_string = input("Enter a string: ")

# Count number of vowels in the input string
num_vowels = count_vowels(input_string)

print(f'The number of vowels in the given string is: {num_vowels}')
