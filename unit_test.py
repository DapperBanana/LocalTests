
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in input_string:
        if char in vowels:
            count += 1
    
    return count

input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))
