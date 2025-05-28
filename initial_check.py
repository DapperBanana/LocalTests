
def count_characters(my_string):
    char_count = {}
    
    for char in my_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

my_string = "Hello, world!"
result = count_characters(my_string)
print(result)
