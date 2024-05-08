
def longest_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = ""
    for i in range(len(min(strings, key=len))):
        if all(strings[j][i] == strings[0][i] for j in range(1, len(strings))):
            prefix += strings[0][i]
        else:
            break
    
    return prefix

# Test the function
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"

strings = ["dog", "racecar", "car"]
print(longest_common_prefix(strings))  # Output: ""
