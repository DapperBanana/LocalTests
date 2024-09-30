
def count_characters(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

if __name__ == "__main__":
    text = input("Enter a string: ")
    result = count_characters(text)

    for char, count in result.items():
        print(f"'{char}' occurs {count} times in the string.")
