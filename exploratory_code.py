
def count_chars(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

string = input("Enter a string: ")
char_counts = count_chars(string)
for char, count in char_counts.items():
    print(f"{char}: {count}")
