
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count

input_text = input("Enter a string: ")
print("Number of vowels in the input string:", count_vowels(input_text))
