
def count_characters(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    result = count_characters(string)
    
    for char, count in result.items():
        print(f"Character '{char}' occurs {count} times in the string.")
