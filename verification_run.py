
def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    
    # Loop through each character in the string
    for char in string:
        if char in vowels:
            count += 1
    
    return count

# Take input from user
input_string = input("Enter a string: ")

# Count the number of vowels in the input string
num_vowels = count_vowels(input_string)

print(f"Number of vowels in the string: {num_vowels}")
