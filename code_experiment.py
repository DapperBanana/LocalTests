
def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

string = input("Enter a string: ")
character_count = count_characters(string)
print("Character count:")
for char, count in character_count.items():
    print(char, ":", count)
