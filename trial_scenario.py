
def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = count_characters(input_string)
    
    print("Character Counts:")
    for char, count in result.items():
        print(f"{char}: {count}")
