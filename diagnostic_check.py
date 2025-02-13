
def count_occurrences(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        print(f"{char}: {count}")

# Test the function with a sample string
s = "hello world"
count_occurrences(s)
