
def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
num_vowels = count_vowels(input_string)
print("Number of vowels in the string:", num_vowels)
