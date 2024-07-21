
def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

input_string = input("Enter a string: ")
if is_isogram(input_string):
    print(f"{input_string} is an isogram.")
else:
    print(f"{input_string} is not an isogram.")
