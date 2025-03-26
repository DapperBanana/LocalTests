
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

input_text = input("Enter a string: ")
num_vowels = count_vowels(input_text)
print("Number of vowels in the given string:", num_vowels)
