
def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

string = input("Enter a string: ")
if is_isogram(string):
    print(f"{string} is an isogram.")
else:
    print(f"{string} is not an isogram.")
