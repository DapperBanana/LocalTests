
def count_characters(s):
    char_counts = {}
    
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

string = "Hello, World!"
result = count_characters(string)

for char, count in result.items():
    print(f"'{char}': {count}")
