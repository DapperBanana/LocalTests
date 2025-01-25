
def is_isogram(s):
    s = s.lower()
    for char in s:
        if s.count(char) > 1:
            return False
    return True

# Input string
string = "programming"

# Check if the string is an isogram
if is_isogram(string):
    print(f"{string} is an isogram")
else:
    print(f"{string} is not an isogram")
