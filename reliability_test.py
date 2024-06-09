
def count_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

input_string = input("Enter a string: ")
result = count_characters(input_string)

for char, count in result.items():
    print(f"'{char}' occurs {count} time(s) in the string.")
