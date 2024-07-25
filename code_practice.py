
def count_characters(s):
    char_count = {}
  
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    return char_count

string = input("Enter a string: ")
result = count_characters(string)

for char, count in result.items():
    print(f"{char}: {count}")
