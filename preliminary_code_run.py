
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
num_vowels = count_vowels(string)
print(f"The number of vowels in the string is: {num_vowels}")