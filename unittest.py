
def count_characters(string):
    character_count = {}

    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

string = "Hello, World!"
result = count_characters(string)

for char, count in result.items():
    print(f"{char}: {count}")
